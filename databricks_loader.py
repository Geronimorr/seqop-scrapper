# -*- coding: utf-8 -*-
"""
Databricks SQL Connector — busca geometria, trajetória, fluidos e info do poço.

Uso:
    from Simulador.data.databricks_loader import DatabricksWellLoader

    loader = DatabricksWellLoader(
        server_hostname="adb-671799829240675.15.azuredatabricks.net",
        http_path="/sql/1.0/warehouses/1fd972f888afd086",
    )
    # Trajetória direcional
    df_dir = loader.get_direcional("1-RJS-763DA")

    # Geometria as-built (revestimentos / tubulares)
    df_rev = loader.get_revestimento("1-RJS-763DA")

    # Fases do poço (seções de diâmetro)
    df_fase = loader.get_fase("1-RJS-763DA")

    # Fluidos de perfuração (reologia, Fann, densidade)
    df_flu = loader.get_fluidos("1-RJS-763DA")

    # Informações gerais do poço (LDA, bacia, sonda, etc.)
    info = loader.get_info_poco("1-RJS-763DA")

O token é lido de variável de ambiente DATABRICKS_TOKEN (recomendado)
ou pode ser passado explicitamente via parâmetro.
"""
from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import Dict, Optional

import pandas as pd

logger = logging.getLogger(__name__)


@dataclass
class DatabricksWellLoader:
    """Conecta ao Databricks SQL e baixa dados de geometria / direcional."""

    server_hostname: str
    http_path: str
    access_token: Optional[str] = None
    catalog: str = "dt0013_prd"
    schema: str = "poco_as_built"
    table_direcional: str = "direcionais"
    table_revestimento: str = "revestimento_poco"
    table_fase: str = "fase_poco"

    # Geoscience tables — FQNs (catalog.schema.table) pois usam catálogos/schemas diferentes
    fqn_pore_frac: str = "dt0013_prd.projeto_poco.pocoweb_projetos_maxima_pressao_cabeca_poco"
    fqn_geothermal: str = "dt0003_prd.projeto_locacao.locacao_dp_gradiente_geoterm"
    fqn_locacao_dp: str = "dt0003_prd.projeto_locacao.locacao_dp"
    fqn_locacao: str = "dt0003_prd.projeto_locacao.locacao"
    fqn_lotfit: str = "dt0013_prd.poco_as_built.lotfit"
    fqn_static_pressure: str = "dt0003_prd.avaliacao.relatorio_pressao_estatica"
    fqn_vinculacao: str = "dt0013_prd.registros_operacionais.intervencao_vinculacao"
    fqn_mesa_rotativa: str = "dt0013_prd.registros_operacionais.mesa_rotativa"

    def __post_init__(self):
        if not self.access_token:
            self.access_token = os.environ.get("DATABRICKS_TOKEN")
        if not self.access_token:
            raise ValueError(
                "Token Databricks não fornecido. Defina a variável de ambiente "
                "DATABRICKS_TOKEN ou passe access_token= no construtor."
            )

    # ------------------------------------------------------------------
    # Conexão
    # ------------------------------------------------------------------
    @staticmethod
    def _safe_name(nome_poco: str) -> str:
        """Sanitiza e normaliza nome para uso em queries SQL."""
        clean = nome_poco.strip().upper().replace("'", "''")
        return clean

    @staticmethod
    def _resolve_col(df: "pd.DataFrame", *aliases) -> Optional[str]:
        """Resolve a column name from a list of aliases (case-insensitive).

        Returns the first matching column name found in the DataFrame,
        or None if none of the aliases match.
        """
        cols_upper = {c.upper(): c for c in df.columns}
        for alias in aliases:
            if alias in df.columns:
                return alias
            real = cols_upper.get(alias.upper())
            if real is not None:
                return real
        return None

    def _connect(self):
        from databricks import sql as dbsql

        return dbsql.connect(
            server_hostname=self.server_hostname,
            http_path=self.http_path,
            access_token=self.access_token,
        )

    def _find_well_column(self, table_fqn: str, conn) -> Optional[str]:
        """Descobre qual coluna contém o nome do poço em uma tabela.

        Tenta variantes comuns no modelo Petrobras: NM_POCO, SG_POCO, CD_POCO.
        Usa DESCRIBE TABLE para listar colunas disponíveis.
        """
        candidates = ['NM_POCO', 'SG_POCO', 'CD_POCO', 'NM_POÇO']
        try:
            cursor = conn.cursor()
            cursor.execute(f"DESCRIBE TABLE {table_fqn}")
            cols_upper = {row[0].upper() for row in cursor.fetchall()}
            cursor.close()
            for c in candidates:
                if c.upper() in cols_upper:
                    return c
            logger.warning(
                "[DESCRIBE] Tabela '%s' não tem coluna de poço. "
                "Colunas disponíveis: %s", table_fqn, sorted(cols_upper),
            )
        except Exception as e:
            logger.warning("DESCRIBE TABLE %s falhou: %s", table_fqn, e)
        return None

    # ------------------------------------------------------------------
    # Direcional (survey)
    # ------------------------------------------------------------------
    def get_direcional(self, nome_poco: str) -> pd.DataFrame:
        """
        Busca dados de survey direcional (MD, inclinação, azimute, TVD, …).

        Colunas retornadas (entre outras):
            MD_PROFUNDIDADE_MEDIDA, MD_INCLINACAO, MD_AZIMUTE,
            MD_PROFUNDIDADE_VERTICAL, MD_DOGLEG_SEVERITY
        """
        fqn = f"{self.catalog}.{self.schema}.{self.table_direcional}"
        safe = self._safe_name(nome_poco)
        query = f"SELECT * FROM {fqn} WHERE UPPER(NM_POCO) = '{safe}' ORDER BY MD_PROFUNDIDADE_MEDIDA"
        conn = self._connect()
        try:
            logger.info("Consultando direcional para '%s' ...", nome_poco)
            df = pd.read_sql(query, conn)
            logger.info("Retornadas %d linhas de direcional.", len(df))
            return df
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Revestimento (casing strings)
    # ------------------------------------------------------------------
    def get_revestimento(self, nome_poco: str) -> pd.DataFrame:
        """
        Busca dados de revestimento as-built.

        Colunas-chave:
            NM_ASSEMBLY, NM_GRUPO_COMPONENTE, NM_COMPONENTE,
            MD_OD_ASSEMBLY, MD_OD_COMPONENTE, ID_BODY, ID_DRIFT,
            MD_TOP, MD_BASE, MD_TVD_TOP_CALCULADO, MD_TVD_BASE_CALCULADO,
            MD_SAPATA, MD_TVD_SAPATA, MD_DIAMETRO_FASE
        """
        fqn = f"{self.catalog}.{self.schema}.{self.table_revestimento}"
        safe = self._safe_name(nome_poco)
        query = f"SELECT * FROM {fqn} WHERE UPPER(NM_POCO) = '{safe}' ORDER BY MD_TOP"
        conn = self._connect()
        try:
            logger.info("Consultando revestimento para '%s' ...", nome_poco)
            df = pd.read_sql(query, conn)
            logger.info("Retornadas %d linhas de revestimento.", len(df))
            return df
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Fase do poço (hole sections)
    # ------------------------------------------------------------------
    def get_fase(self, nome_poco: str) -> pd.DataFrame:
        """
        Busca dados de fase do poço (seções de diâmetro).

        Colunas-chave:
            NR_FASE, MD_DIAMETRO_FASE, MD_PROF_TOPO_FASE, MD_PROF_BASE_FASE,
            MD_TVD_TOPO, MD_TVD_BASE, MD_DIAMETRO_EXTERNO (OD revestimento),
            MD_DIAMETRO_INTERNO, TX_MPD
        """
        fqn = f"{self.catalog}.{self.schema}.{self.table_fase}"
        safe = self._safe_name(nome_poco)
        query = f"SELECT * FROM {fqn} WHERE UPPER(NM_POCO) = '{safe}' ORDER BY NR_FASE"
        conn = self._connect()
        try:
            logger.info("Consultando fases para '%s' ...", nome_poco)
            df = pd.read_sql(query, conn)
            logger.info("Retornadas %d fases.", len(df))
            return df
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Fluidos de perfuração
    # ------------------------------------------------------------------
    def get_fluidos(self, nome_poco: str, fase: Optional[int] = None) -> pd.DataFrame:
        """
        Busca dados de fluidos de perfuração.

        Colunas-chave:
            NR_FASE, TX_BASE_FLUIDO, TX_TIPO_FLUIDO,
            MD_PROFUNDIDADE_FLUIDO, MD_DENSIDADE (ppg),
            MD_VISCOSIDADE_PLASTICA (cP), MD_LIM_ESCOAMENTO (lbf/100ft²),
            MD_GELS_10_SEC, MD_GELS_10_MIN, MD_GELS_30_MIN (lbf/100ft²),
            MD_RPM_3, MD_RPM_6, MD_RPM_100, MD_RPM_200, MD_RPM_300, MD_RPM_600
        """
        fqn = f"{self.catalog}.registros_operacionais.fluidos"
        safe = self._safe_name(nome_poco)
        where = f"UPPER(NM_POCO) = '{safe}'"
        if fase is not None:
            where += f" AND NR_FASE = {int(fase)}"
        # ORDER BY: try DT_COLETA first, fall back to NR_FASE only
        base_query = f"SELECT * FROM {fqn} WHERE {where}"
        logger.info("Consultando fluidos para '%s' (fase=%s) ...", nome_poco, fase)
        for order_by in [
            " ORDER BY NR_FASE, DT_COLETA",
            " ORDER BY NR_FASE, DT_BOLETIM",
            " ORDER BY NR_FASE",
            "",
        ]:
            conn = self._connect()
            try:
                df = pd.read_sql(base_query + order_by, conn)
                logger.info("Retornados %d registros de fluidos.", len(df))
                return df
            except Exception:
                pass
            finally:
                try:
                    conn.close()
                except Exception:
                    pass
        # Should not reach here, but return empty as safety
        return pd.DataFrame()

    # ------------------------------------------------------------------
    # Informações gerais do poço
    # ------------------------------------------------------------------
    def get_info_poco(self, nome_poco: str) -> Optional[Dict]:
        """
        Busca informações gerais do poço.

        Campos de interesse:
            MD_LAMINA_DAGUA (m) — lâmina d'água (= LDA para o simulador),
            MD_MESA_ROTATIVA_METRO (m), NM_SONDA_REFERENCIA,
            NM_BACIA, NM_COMPLETO_CAMPO, IN_PRE_SAL,
            MD_PROFUNDIDADE_FINAL (m), MD_INCLINACAO_MAX (°)
        """
        fqn = f"{self.catalog}.informacoes_gerais_poco.poco"
        safe = self._safe_name(nome_poco)
        query = f"SELECT * FROM {fqn} WHERE UPPER(NM_POCO) = '{safe}'"
        conn = self._connect()
        try:
            logger.info("Consultando info do poço '%s' ...", nome_poco)
            cursor = conn.cursor()
            cursor.execute(query)
            cols = [d[0] for d in cursor.description]
            row = cursor.fetchone()
            cursor.close()
            if row:
                info = dict(zip(cols, row))
                logger.info(
                    "Poço '%s': bacia=%s, sonda=%s, LDA=%.0f m",
                    nome_poco,
                    info.get("NM_BACIA", "?"),
                    info.get("NM_SONDA_REFERENCIA", "?"),
                    info.get("MD_LAMINA_DAGUA") or 0,
                )
                return info
            logger.warning("Poço '%s' não encontrado em informacoes_gerais_poco.", nome_poco)
            return None
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Montar WellGeometry a partir dos dados
    # ------------------------------------------------------------------
    def build_well_geometry(
        self,
        nome_poco: str,
        bit_depth_m: Optional[float] = None,
        lda_m: Optional[float] = None,
        bha_len_m: float = 114.0,
        bha_od_segments: Optional[list] = None,
    ):
        """
        Consulta Databricks e monta um WellGeometry pronto para o simulador.

        Usa tabelas: direcionais (TVD), fase_poco (diâmetros e sapata),
        revestimento_poco (ID do revestimento), informacoes_gerais_poco.poco (LDA).

        Se lda_m não for passado, tenta extrair MD_LAMINA_DAGUA da tabela
        de informações gerais do poço.

        Retorna:
            (WellGeometry, df_direcional, df_revestimento, df_fase, info_poco)
        """
        from Simulador.physics.well_geometry import WellGeometry
        from Simulador.core import constants as C

        df_dir = self.get_direcional(nome_poco)
        df_rev = self.get_revestimento(nome_poco)
        df_fase = self.get_fase(nome_poco)
        info_poco = self.get_info_poco(nome_poco)

        # --- TVD do fundo (última linha do direcional) ---
        if df_dir.empty or "MD_PROFUNDIDADE_VERTICAL" not in df_dir.columns:
            raise KeyError(
                f"Dados de direcional não encontrados para '{nome_poco}'. "
                f"Colunas disponíveis: {list(df_dir.columns)}"
            )

        tvd_m = float(df_dir["MD_PROFUNDIDADE_VERTICAL"].max())
        md_max = float(df_dir["MD_PROFUNDIDADE_MEDIDA"].max())
        if bit_depth_m is None:
            bit_depth_m = tvd_m

        # Defaults do constants.py como fallback
        cfg = C.WellGeometryConfig
        casing_shoe_m = cfg.CASING_SHOE_DEPTH_M
        diam_casing_in = cfg.DIAM_ID_CASING_IN
        diam_riser_in = cfg.DIAM_ID_RISER_IN
        diam_open_hole_in = cfg.DIAM_ID_OPEN_HOLE_IN
        od_dp_in = cfg.DIAM_OD_DP_IN
        od_bha_in = cfg.DIAM_OD_BHA_IN

        # --- Extrair da tabela fase_poco ---
        # Fase com MPD = SIM e maior profundidade é a fase atual
        if not df_fase.empty:
            # Última fase (maior NR_FASE) = fase atual de perfuração
            last_fase = df_fase.iloc[-1]
            diam_open_hole_in = float(last_fase["MD_DIAMETRO_FASE"])

            # OD do revestimento da última fase (= OD da coluna de drill string superior)
            if pd.notna(last_fase.get("MD_DIAMETRO_EXTERNO")):
                od_bha_in_fase = float(last_fase["MD_DIAMETRO_EXTERNO"])

            # Sapata = base do revestimento da fase anterior (penúltima fase)
            # Try multiple column names for robustness
            if len(df_fase) >= 2:
                prev_fase = df_fase.iloc[-2]
                shoe_found = False
                for shoe_col in ("MD_BASE_REVESTIMENTO", "MD_SAPATA",
                                 "MD_PROF_BASE_FASE"):
                    val = prev_fase.get(shoe_col)
                    if val is not None and pd.notna(val):
                        casing_shoe_m = float(val)
                        shoe_found = True
                        logger.info("Sapata obtida de fase_poco.%s: %.1f m", shoe_col, casing_shoe_m)
                        break
                if not shoe_found:
                    # Fallback: max MD_SAPATA from revestimento table matching prev phase
                    if not df_rev.empty:
                        for sap_col in ("MD_SAPATA", "MD_BASE"):
                            if sap_col in df_rev.columns:
                                sapatas = df_rev[sap_col].dropna()
                                if not sapatas.empty:
                                    casing_shoe_m = float(sapatas.max())
                                    logger.info("Sapata obtida de revestimento.%s (max): %.1f m",
                                                sap_col, casing_shoe_m)
                                    shoe_found = True
                                    break

        # --- Extrair ID body do revestimento ---
        # Robust: try multiple column names for assembly/group identification
        if not df_rev.empty and "ID_BODY" in df_rev.columns:
            group_col = None
            for gc in ("NM_GRUPO_COMPONENTE", "NM_ASSEMBLY", "NM_COMPONENTE"):
                if gc in df_rev.columns:
                    group_col = gc
                    break

            if group_col:
                mask_rev = df_rev[group_col].astype(str).str.upper().str.contains(
                    "REVESTIMENTO", na=False
                )
            else:
                # No group column — use all rows that have ID_BODY
                mask_rev = pd.Series(True, index=df_rev.index)

            rev_rows = df_rev.loc[mask_rev & df_rev["ID_BODY"].notna()]
            if not rev_rows.empty:
                # Pick the casing just above current open hole
                # (last record before the current phase shoe depth)
                last_rev = rev_rows.iloc[-1]
                diam_casing_in = float(last_rev["ID_BODY"])
                logger.info("Casing ID extraído de revestimento: %.3f in", diam_casing_in)

        if lda_m is None:
            # Tentar extrair LDA da tabela informacoes_gerais_poco
            if info_poco and info_poco.get("MD_LAMINA_DAGUA"):
                lda_m = float(info_poco["MD_LAMINA_DAGUA"])
                logger.info("LDA extraída do Databricks: %.1f m", lda_m)
            else:
                lda_m = cfg.LENGTH_LDA_M

        # --- Air Gap (mesa rotativa → nível do mar) ---
        air_gap_m = 0.0
        sonda_referencia = None
        if info_poco:
            mr = info_poco.get("MD_MESA_ROTATIVA_METRO")
            if mr is not None and pd.notna(mr):
                air_gap_m = float(mr)
            sr = info_poco.get("NM_SONDA_REFERENCIA")
            if sr:
                sonda_referencia = str(sr).strip()
            logger.info(
                "Air Gap (mesa rotativa): %.1f m, sonda ref: %s",
                air_gap_m, sonda_referencia or "?",
            )

        wg = WellGeometry(
            tvd_m=tvd_m,
            bit_depth_m=bit_depth_m,
            lda_m=lda_m,
            casing_shoe_depth_m=casing_shoe_m,
            bha_len_m=bha_len_m,
            diam_open_hole_in=diam_open_hole_in,
            diam_casing_in=diam_casing_in,
            diam_riser_in=diam_riser_in,
            od_dp_in=od_dp_in,
            od_bha_in=od_bha_in,
            bha_od_segments=bha_od_segments,
            air_gap_m=air_gap_m,
            sonda_referencia=sonda_referencia,
        )

        # --- Trajetória direcional (MD → TVD) ---
        if not df_dir.empty:
            col_md = "MD_PROFUNDIDADE_MEDIDA"
            col_tvd = "MD_PROFUNDIDADE_VERTICAL"
            if col_md in df_dir.columns and col_tvd in df_dir.columns:
                valid = df_dir[[col_md, col_tvd]].dropna()
                if len(valid) >= 2:
                    wg.set_trajectory(
                        valid[col_md].astype(float).values,
                        valid[col_tvd].astype(float).values,
                    )

        logger.info(
            "WellGeometry construída: TVD=%.1f m, bit=%.1f m, sapata=%.1f m, "
            "LDA=%.1f m, OH=%.2f\", casing_ID=%.3f\", air_gap=%.1f m, traj=%s",
            tvd_m, bit_depth_m, casing_shoe_m, lda_m, diam_open_hole_in, diam_casing_in,
            air_gap_m, "sim" if wg.has_trajectory else "não",
        )
        return wg, df_dir, df_rev, df_fase, info_poco

    # ------------------------------------------------------------------
    # BHA OD profile (multi-OD segments)
    # ------------------------------------------------------------------
    def build_bha_od_profile(
        self, nome_poco: str, diam_open_hole_in: float = 12.25,
        bha_df: "pd.DataFrame | None" = None,
    ) -> "list[tuple[float, float]]":
        """Agrupa componentes do BHA por OD e retorna perfil multi-OD.

        Retorna lista de (od_in, length_m) do fundo (broca) para o topo.
        Componentes com OD >= diâmetro do poço aberto (broca) são excluídos.
        ODs consecutivos iguais são fundidos em um único segmento.

        Se ``bha_df`` for fornecido, usa esse DataFrame diretamente
        (já filtrado para o BHA run desejado) em vez de buscar no DB.
        """
        from typing import List, Tuple

        if bha_df is not None:
            bha = bha_df.copy()
        else:
            df_bha = self.get_bha(nome_poco)
            if df_bha.empty:
                return []
            # Usar último BHA run
            latest_run = df_bha["BHA_RUN_ID"].unique()[-1]
            bha = df_bha[df_bha["BHA_RUN_ID"] == latest_run].copy()
        bha = bha.sort_values("NR_ORDEM_COMPONENTES")

        # Excluir broca (OD >= hole diameter) e componentes sem OD/comprimento
        segments: List[Tuple[float, float]] = []
        for _, row in bha.iterrows():
            od = row.get("MD_DIAMETRO_EXTERNO")
            length = row.get("MD_COMPRIMENTO")
            if pd.isna(od) or pd.isna(length) or float(od) <= 0 or float(length) <= 0:
                continue
            od = float(od)
            length = float(length)
            if od >= diam_open_hole_in:
                continue  # broca — mesma dimensão do poço, sem espaço anular
            segments.append((od, length))

        if not segments:
            return []

        # Fundir ODs consecutivos iguais (tolerância 0.01")
        merged: List[Tuple[float, float]] = [segments[0]]
        for od, length in segments[1:]:
            if abs(od - merged[-1][0]) < 0.01:
                merged[-1] = (merged[-1][0], merged[-1][1] + length)
            else:
                merged.append((od, length))

        # A tabela BHA está ordenada do fundo (broca) para o topo
        # (NR_ORDEM_COMPONENTES crescente = do fundo para cima)
        logger.info(
            "BHA OD profile (%d zonas): %s",
            len(merged),
            " | ".join(f'{od:.3f}\"×{L:.1f}m' for od, L in merged),
        )
        return merged

    # ------------------------------------------------------------------
    # Tempos de operações (activity log with depth-time correlation)
    # ------------------------------------------------------------------
    def get_tempos_operacoes(
        self, nome_poco: str, fase: Optional[int] = None
    ) -> pd.DataFrame:
        """
        Busca log de atividades com correlação profundidade × tempo.

        Colunas-chave:
            DT_INICIO_ATIVIDADE, DT_FIM_ATIVIDADE,
            MD_PROFUNDIDADE_INICIAL, MD_PROFUNDIDADE_FINAL,
            MD_DURACAO_TOTAL (h), TX_ATIVIDADE, TX_OPERACAO, TX_ETAPA,
            NR_FASE, IN_TIPO_TEMPO
        """
        fqn = f"{self.catalog}.registros_operacionais.tempos_operacoes_completa"
        safe = self._safe_name(nome_poco)
        where = f"UPPER(NM_POCO) = '{safe}'"
        if fase is not None:
            where += f" AND NR_FASE = {int(fase)}"
        query = f"SELECT * FROM {fqn} WHERE {where} ORDER BY DT_INICIO_ATIVIDADE"
        conn = self._connect()
        try:
            logger.info(
                "Consultando tempos_operacoes para '%s' (fase=%s) ...",
                nome_poco, fase,
            )
            df = pd.read_sql(query, conn)
            logger.info("Retornados %d registros de tempos_operacoes.", len(df))
            return df
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # BHA (Bottom Hole Assembly)
    # ------------------------------------------------------------------
    def get_bha(self, nome_poco: str) -> pd.DataFrame:
        """
        Busca componentes do BHA.

        Colunas-chave:
            TX_GRUPO_COMPONENTE, NM_COMPONENTE,
            MD_DIAMETRO_EXTERNO (in), MD_DIAMETRO_INTERNO (in),
            MD_COMPRIMENTO (m), MD_PESO_APROXIMADO (lbs),
            NR_ORDEM_COMPONENTES, DT_ENTRADA, DT_SAIDA,
            MD_TOPO_INTERVALO, MD_BASE_INTERVALO
        """
        fqn = f"{self.catalog}.registros_operacionais.bha"
        safe = self._safe_name(nome_poco)
        query = (
            f"SELECT * FROM {fqn} WHERE UPPER(NM_POCO) = '{safe}' "
            f"ORDER BY BHA_RUN_ID, NR_ORDEM_COMPONENTES"
        )
        conn = self._connect()
        try:
            logger.info("Consultando BHA para '%s' ...", nome_poco)
            df = pd.read_sql(query, conn)
            logger.info("Retornados %d componentes de BHA.", len(df))
            return df
        finally:
            conn.close()

    # ------------------------------------------------------------------
    # Timeline de profundidade (depth vs time from activity log)
    # ------------------------------------------------------------------
    def build_depth_timeline(
        self, nome_poco: str, fase: Optional[int] = None
    ) -> pd.DataFrame:
        """
        Constrói um timeline contínuo de profundidade × tempo a partir
        do log de atividades (tempos_operacoes_completa).

        Retorna DataFrame com colunas:
            timestamp, bit_depth_m
        onde cada linha é um marco de profundidade (início ou fim de
        atividade com profundidade registrada).
        Registros sem profundidade (circulação, manobra, etc.)
        são preenchidos por forward-fill.
        """
        import numpy as np

        df = self.get_tempos_operacoes(nome_poco, fase=fase)
        if df.empty:
            return pd.DataFrame(columns=["timestamp", "bit_depth_m"])

        points = []
        for _, row in df.iterrows():
            t_ini = row.get("DT_INICIO_ATIVIDADE")
            t_fim = row.get("DT_FIM_ATIVIDADE")
            d_ini = row.get("MD_PROFUNDIDADE_INICIAL")
            d_fim = row.get("MD_PROFUNDIDADE_FINAL")

            if pd.notna(t_ini) and pd.notna(d_ini):
                points.append({"timestamp": pd.Timestamp(t_ini), "bit_depth_m": float(d_ini)})
            if pd.notna(t_fim) and pd.notna(d_fim):
                points.append({"timestamp": pd.Timestamp(t_fim), "bit_depth_m": float(d_fim)})

        if not points:
            return pd.DataFrame(columns=["timestamp", "bit_depth_m"])

        tl = (
            pd.DataFrame(points)
            .sort_values("timestamp")
            .drop_duplicates(subset="timestamp", keep="last")
            .reset_index(drop=True)
        )
        return tl

    # ------------------------------------------------------------------
    # Timeline de fluidos (fluid properties vs time)
    # ------------------------------------------------------------------
    def build_fluid_timeline(
        self, nome_poco: str, fase: Optional[int] = None
    ) -> pd.DataFrame:
        """
        Constrói um timeline de propriedades do fluido × tempo a partir
        da tabela fluidos.

        Retorna DataFrame com colunas:
            timestamp, bit_depth_m, mud_weight_ppg,
            pv_cp, yp_lbf, gel_10s, gel_10min, gel_30min,
            theta_600, theta_300, theta_200, theta_100, theta_6, theta_3
        """
        df = self.get_fluidos(nome_poco, fase=fase)
        if df.empty:
            return pd.DataFrame()

        # Log das colunas disponíveis para diagnóstico
        logger.info(
            "[FLUID_TL] Colunas retornadas pelo Databricks (%d): %s",
            len(df.columns), list(df.columns),
        )

        # Each entry: normalized_name → list of Databricks column aliases
        # (first match wins). Covers known schema variations across wells.
        col_aliases = {
            "timestamp":      ["DT_COLETA", "DT_DATA", "DT_BOLETIM"],
            "bit_depth_m":    ["MD_PROFUNDIDADE_FLUIDO", "MD_PROFUNDIDADE"],
            "mud_weight_ppg": ["MD_DENSIDADE", "MD_PESO_FLUIDO", "MD_PESO"],
            "pv_cp":          ["MD_VISCOSIDADE_PLASTICA", "MD_VIS_PLASTICA", "MD_VP"],
            "yp_lbf":         ["MD_LIM_ESCOAMENTO", "MD_LIMITE_ESCOAMENTO", "MD_LE"],
            "gel_10s":        ["MD_GELS_10_SEC", "MD_GEL_INICIAL", "MD_GEL_10S"],
            "gel_10min":      ["MD_GELS_10_MIN", "MD_GEL_10MIN", "MD_GEL_10_MIN"],
            "gel_30min":      ["MD_GELS_30_MIN", "MD_GEL_30MIN", "MD_GEL_30_MIN"],
            "theta_600":      ["MD_RPM_600"],
            "theta_300":      ["MD_RPM_300"],
            "theta_200":      ["MD_RPM_200"],
            "theta_100":      ["MD_RPM_100"],
            "theta_6":        ["MD_RPM_6"],
            "theta_3":        ["MD_RPM_3"],
        }
        # Build upper-case lookup for case-insensitive matching
        cols_upper_map = {c.upper(): c for c in df.columns}

        out_cols = {}
        missing_cols = []
        for dst, aliases in col_aliases.items():
            found = False
            for alias in aliases:
                # Exact match
                if alias in df.columns:
                    out_cols[dst] = df[alias].values
                    found = True
                    break
                # Case-insensitive match
                real = cols_upper_map.get(alias.upper())
                if real is not None:
                    out_cols[dst] = df[real].values
                    logger.info("[FLUID_TL] '%s' → '%s' (case-insensitive)", alias, real)
                    found = True
                    break
            if not found:
                missing_cols.append(f"{dst} (tried: {aliases})")
        if missing_cols:
            logger.warning(
                "[FLUID_TL] Colunas NÃO encontradas: %s  |  Disponíveis: %s",
                missing_cols, sorted(df.columns.tolist()),
            )

        # Log das colunas Fann mapeadas
        fann_mapped = [k for k in out_cols if k.startswith("theta_")]
        logger.info("[FLUID_TL] Colunas Fann mapeadas: %s", fann_mapped if fann_mapped else "NENHUMA")
        result = pd.DataFrame(out_cols)
        if "timestamp" in result.columns:
            result["timestamp"] = pd.to_datetime(result["timestamp"])
            result = result.sort_values("timestamp").reset_index(drop=True)
        return result

    # ------------------------------------------------------------------
    # Geometria para uma data específica
    # ------------------------------------------------------------------
    def get_geometry_at_date(
        self,
        nome_poco: str,
        target_date: "pd.Timestamp | str",
        bha_len_m: float = 114.0,
    ):
        """
        Retorna (WellGeometry, fluid_info) configurados para uma data
        específica, usando profundidade interpolada e propriedades do
        fluido mais recentes até aquela data.

        Args:
            nome_poco: Nome do poço (NM_POCO)
            target_date: Data alvo (str ou Timestamp)
            bha_len_m: Comprimento do BHA (m)

        Returns:
            dict com chaves:
                'well_geometry': WellGeometry pronta
                'bit_depth_m': profundidade da broca naquela data
                'fluid': dict com mud_weight_ppg, pv_cp, yp_lbf, Fann readings
                'phase': número da fase ativa
                'activity': descrição da atividade naquele momento
        """
        import numpy as np

        target = pd.Timestamp(target_date)

        # 1) Buscar timeline de profundidade (todas as fases)
        depth_tl = self.build_depth_timeline(nome_poco)
        if depth_tl.empty:
            raise ValueError(
                f"Sem dados de tempos_operacoes para '{nome_poco}'. "
                "Não é possível determinar a profundidade nessa data."
            )

        # 2) Interpolar profundidade na data-alvo
        mask_before = depth_tl["timestamp"] <= target
        if not mask_before.any():
            bit_depth = float(depth_tl["bit_depth_m"].iloc[0])
        else:
            last_before = depth_tl.loc[mask_before].iloc[-1]
            mask_after = depth_tl["timestamp"] > target
            if not mask_after.any():
                bit_depth = float(last_before["bit_depth_m"])
            else:
                next_after = depth_tl.loc[mask_after].iloc[0]
                t0 = last_before["timestamp"].timestamp()
                t1 = next_after["timestamp"].timestamp()
                tt = target.timestamp()
                if t1 - t0 > 0:
                    frac = (tt - t0) / (t1 - t0)
                    bit_depth = float(
                        last_before["bit_depth_m"]
                        + frac * (next_after["bit_depth_m"] - last_before["bit_depth_m"])
                    )
                else:
                    bit_depth = float(last_before["bit_depth_m"])

        # 3) Buscar propriedades do fluido mais recentes
        #    Quando há múltiplos fluidos na mesma data (ex.: 2 bases diferentes),
        #    prioriza o que tem leituras Fann (theta_600 != null). Dentre os que
        #    têm Fann, escolhe o mais leve (= fluido ativo no poço aberto).
        fluid_tl = self.build_fluid_timeline(nome_poco)
        fluid_info = {}
        if not fluid_tl.empty and "timestamp" in fluid_tl.columns:
            mask_fl = fluid_tl["timestamp"] <= target
            candidates = fluid_tl.loc[mask_fl]
            if not candidates.empty:
                # Pega o dia mais recente e seleciona todos os fluidos desse dia
                latest_ts = candidates["timestamp"].max()
                same_day = candidates[
                    candidates["timestamp"].dt.date == latest_ts.date()
                ]
                if len(same_day) > 1:
                    # Múltiplos fluidos no mesmo dia — priorizar por Fann
                    fann_cols = ["theta_600", "theta_300", "theta_200",
                                 "theta_100", "theta_6", "theta_3"]
                    existing_fann = [c for c in fann_cols if c in same_day.columns]
                    if existing_fann:
                        same_day = same_day.copy()
                        same_day["_fann_count"] = same_day[existing_fann].notna().sum(axis=1)
                        max_fann = same_day["_fann_count"].max()
                        with_fann = same_day[same_day["_fann_count"] == max_fann]
                    else:
                        with_fann = same_day

                    # Dentre os que têm mais Fann, pega o último do dia (mais recente)
                    best = with_fann.iloc[-1]

                    logger.info(
                        "[FLUID SELECT] %d fluidos em %s — escolhido MW=%.2f ppg "
                        "com %d leituras Fann (de %d candidatos)",
                        len(same_day), latest_ts.date(),
                        best.get("mud_weight_ppg", 0),
                        best.get("_fann_count", 0) if "_fann_count" in best.index else 0,
                        len(same_day),
                    )
                    fl_row = best.to_dict()
                else:
                    fl_row = same_day.iloc[-1].to_dict()

                fluid_info = {k: v for k, v in fl_row.items()
                              if k != "timestamp" and not str(k).startswith("_")
                              and pd.notna(v)}

        # 4) Determinar fase ativa
        df_fase = self.get_fase(nome_poco)
        phase_num = None
        if not df_fase.empty and "DT_INICIO_FASE" in df_fase.columns:
            for _, frow in df_fase.iterrows():
                dt_ini = pd.Timestamp(frow["DT_INICIO_FASE"])
                dt_fim = pd.Timestamp(frow.get("DT_FIM_FASE", pd.NaT))
                if dt_ini <= target and (pd.isna(dt_fim) or target <= dt_fim):
                    phase_num = int(frow["NR_FASE"])
                    break

        # 5) Construir geometria com a profundidade interpolada
        wg, _df_dir, _df_rev, _df_fase, _info = self.build_well_geometry(
            nome_poco, bit_depth_m=bit_depth, bha_len_m=bha_len_m,
        )

        return {
            "well_geometry": wg,
            "bit_depth_m": bit_depth,
            "fluid": fluid_info,
            "phase": phase_num,
            "target_date": target,
        }

    # ==================================================================
    # Pore & Fracture pressure (pocoweb_projetos_maxima)
    # ==================================================================
    def get_pore_frac_pressure(self, nome_poco: str) -> pd.DataFrame:
        """
        Busca curvas de pressão de poro e fratura (janela operacional).

        Colunas-chave:
            MD_PROFUNDIDADE_VERTICAL_CALCULO — TVD [m],
            MD_PRESSAO_POROS_EQUIVALENTE_CORRESPONDENTE — pressão de poro [lb/gal],
            MD_PRESSAO_FRATURA_EQUIVALENTE_SAPATA — pressão de fratura [lb/gal],
            MD_TEMPERATURA_CORRESPONDENTE — temperatura [°C],
            MD_BASE_COTA, MD_TOPO_SEGMENTO_COTA — cotas [m]
        """
        safe = self._safe_name(nome_poco)
        query = (
            f"SELECT * FROM {self.fqn_pore_frac} WHERE UPPER(NM_POCO) = '{safe}' "
            f"ORDER BY MD_PROFUNDIDADE_VERTICAL_CALCULO"
        )
        conn = self._connect()
        try:
            logger.info("Consultando pore/frac pressure para '%s' ...", nome_poco)
            df = pd.read_sql(query, conn)
            logger.info("Retornadas %d linhas de pore/frac.", len(df))
            return df
        finally:
            conn.close()

    def build_pore_frac_profiles(
        self, nome_poco: str
    ) -> "dict[str, list[tuple[float, float]]]":
        """
        Constrói perfis de pressão de poro e fratura como listas de
        (profundidade_m, gradiente_ppg) prontas para FormationConfig.

        Returns:
            dict com chaves:
                'pore': [(depth_m, ppg), ...]
                'frac': [(depth_m, ppg), ...]
            Listas vazias se não houver dados.
        """
        df = self.get_pore_frac_pressure(nome_poco)
        result: dict = {"pore": [], "frac": []}
        if df.empty:
            return result

        col_tvd = "MD_PROFUNDIDADE_VERTICAL_CALCULO"
        col_pore = "MD_PRESSAO_POROS_EQUIVALENTE_CORRESPONDENTE"
        col_frac = "MD_PRESSAO_FRATURA_EQUIVALENTE_SAPATA"

        if col_tvd not in df.columns:
            logger.warning("[PORE_FRAC] Coluna TVD '%s' não encontrada.", col_tvd)
            return result

        for _, row in df.iterrows():
            tvd = row.get(col_tvd)
            if pd.isna(tvd):
                continue
            tvd = float(tvd)

            pore = row.get(col_pore)
            if pd.notna(pore):
                result["pore"].append((tvd, float(pore)))

            frac = row.get(col_frac)
            if pd.notna(frac):
                result["frac"].append((tvd, float(frac)))

        logger.info(
            "[PORE_FRAC] Perfis construídos: %d pontos poro, %d pontos fratura",
            len(result["pore"]), len(result["frac"]),
        )
        return result

    # ==================================================================
    # Geothermal profile
    # ==================================================================
    def get_geothermal(self, nome_poco: str) -> pd.DataFrame:
        """
        Busca perfil geotérmico (temperatura × profundidade).

        A tabela geothermal não possui NM_POCO diretamente — é filha de
        locacao_dp, que por sua vez é filha de locacao (que tem NM_POCO).
        JOIN: gradiente_geoterm → locacao_dp → locacao.

        Colunas-chave:
            MD_COTA — profundidade / cota [m],
            MD_TEMPERATURA — temperatura [°C]
        """
        safe = self._safe_name(nome_poco)
        query = (
            f"SELECT gt.* FROM {self.fqn_geothermal} gt "
            f"JOIN {self.fqn_locacao_dp} dp ON gt.LODP_SQ_LOCACAO_DP = dp.SQ_LOCACAO_DP "
            f"JOIN {self.fqn_locacao} loc ON dp.LOCC_SQ_LOCACAO = loc.SQ_LOCACAO "
            f"WHERE UPPER(loc.NM_POCO) = '{safe}' "
            f"ORDER BY gt.MD_COTA"
        )
        conn = self._connect()
        try:
            logger.info("Consultando geothermal para '%s' (via JOIN locacao) ...", nome_poco)
            df = pd.read_sql(query, conn)
            logger.info("Retornadas %d linhas de geothermal.", len(df))
            return df
        finally:
            conn.close()

    def build_geothermal_profile(self, nome_poco: str):
        """
        Constrói um GeothermalProfile a partir dos dados Databricks.

        Returns:
            GeothermalProfile com perfil tabelado, ou None se sem dados.
        """
        import numpy as np
        from Simulador.physics.thermal_profile import GeothermalProfile

        df = self.get_geothermal(nome_poco)
        if df.empty:
            logger.info("[GEOTHERMAL] Sem dados Databricks — usando perfil analítico.")
            return None

        col_depth = "MD_COTA"
        col_temp = "MD_TEMPERATURA"

        if col_depth not in df.columns or col_temp not in df.columns:
            logger.warning(
                "[GEOTHERMAL] Colunas esperadas ('%s', '%s') não encontradas. "
                "Disponíveis: %s", col_depth, col_temp, list(df.columns),
            )
            return None

        valid = df[[col_depth, col_temp]].dropna()
        if valid.empty:
            return None

        depths = valid[col_depth].astype(float).values
        temps = valid[col_temp].astype(float).values

        # Garantir ordem crescente de profundidade
        order = np.argsort(depths)
        depths = depths[order]
        temps = temps[order]

        profile = GeothermalProfile(depths_m=depths, temperatures_c=temps)
        logger.info(
            "[GEOTHERMAL] Perfil carregado do Databricks: %d pontos, "
            "%.0f–%.0f m, %.1f–%.1f °C",
            len(depths), depths[0], depths[-1], temps.min(), temps.max(),
        )
        return profile

    # ==================================================================
    # LOT / FIT tests
    # ==================================================================
    def get_lotfit(self, nome_poco: str) -> pd.DataFrame:
        """
        Busca resultados de testes LOT (Leak-Off Test) e FIT (Formation
        Integrity Test).

        Colunas-chave:
            TX_TIPO_TESTE — tipo ('LOT', 'FIT' ou 'FIT+'),
            MD_PRESSAO_SAPATA — pressão na sapata [psi],
            MD_PESO_FLUIDO_EQUIV — peso de fluido equivalente [lb/gal],
            MD_PROF_SAPATA — profundidade da sapata [m MD],
            MD_PROF_TVD_SAPATA — profundidade da sapata [m TVD]
        """
        safe = self._safe_name(nome_poco)
        query = (
            f"SELECT * FROM {self.fqn_lotfit} WHERE UPPER(NM_POCO) = '{safe}' "
            f"ORDER BY MD_PROF_SAPATA"
        )
        conn = self._connect()
        try:
            logger.info("Consultando LOT/FIT para '%s' ...", nome_poco)
            df = pd.read_sql(query, conn)
            logger.info("Retornados %d registros de LOT/FIT.", len(df))
            return df
        finally:
            conn.close()

    # ==================================================================
    # Static pressure (pressão estática)
    # ==================================================================
    def get_static_pressure(self, nome_poco: str) -> pd.DataFrame:
        """
        Busca medições de pressão estática no poço.

        A tabela pode não ter 'NM_POCO' — descobre a coluna de poço
        via DESCRIBE TABLE e tenta variantes (NM_POCO, SG_POCO, CD_POCO).

        Colunas-chave:
            MD_PRSS_ESTT_REGT — pressão estática registrada [psi],
            MD_PROF_VERT_REGT — profundidade vertical registrada [m TVD]
        """
        safe = self._safe_name(nome_poco)
        conn = self._connect()
        try:
            # Descobrir coluna de poço na tabela
            well_col = self._find_well_column(self.fqn_static_pressure, conn)
            if well_col is None:
                logger.warning(
                    "[STATIC_PRESSURE] Nenhuma coluna de poço encontrada em '%s'. "
                    "Tabela não suportada para filtro por poço.",
                    self.fqn_static_pressure,
                )
                return pd.DataFrame()

            query = (
                f"SELECT * FROM {self.fqn_static_pressure} "
                f"WHERE UPPER({well_col}) = '{safe}' "
                f"ORDER BY MD_PROF_VERT_REGT"
            )
            logger.info(
                "Consultando pressão estática para '%s' (col=%s) ...",
                nome_poco, well_col,
            )
            df = pd.read_sql(query, conn)
            logger.info("Retornados %d registros de pressão estática.", len(df))
            return df
        finally:
            conn.close()

    # ==================================================================
    # Vinculação sonda–poço (rig assignment history)
    # ==================================================================
    def get_vinculacao_sonda(self, nome_poco: str) -> pd.DataFrame:
        """
        Busca histórico de vinculação sonda–poço com Air Gap (LEFT JOIN
        mesa_rotativa via WELL_ID + RIG_ID).

        Colunas retornadas (entre outras):
            NM_SONDA — nome da sonda,
            DT_INICIO_VINCULACAO — início da vinculação,
            DT_FIM_VINCULACAO — fim da vinculação (NaT se ativa),
            TX_TIPO_EVENTO — tipo (perfuração, completação, etc.),
            MD_AIR_GAP — Air Gap da sonda [m] (pode ser NULL),
            MD_DATUM_ELEVACAO — elevação do datum [m],
            IN_DEFAULT — primeira sonda no poço (boolean)
        """
        safe = self._safe_name(nome_poco)
        query = (
            f"SELECT iv.*, mr.MD_AIR_GAP, mr.MD_DATUM_ELEVACAO, mr.IN_DEFAULT "
            f"FROM {self.fqn_vinculacao} iv "
            f"LEFT JOIN {self.fqn_mesa_rotativa} mr "
            f"  ON iv.WELL_ID = mr.WELL_ID AND iv.RIG_ID = mr.RIG_ID "
            f"WHERE UPPER(iv.NM_POCO) = '{safe}' "
            f"ORDER BY iv.DT_INICIO_VINCULACAO"
        )
        conn = self._connect()
        try:
            logger.info("Consultando vinculação+mesa_rotativa para '%s' ...", nome_poco)
            df = pd.read_sql(query, conn)
            logger.info("Retornados %d registros de vinculação.", len(df))
            return df
        finally:
            conn.close()

    def get_sonda_at_date(
        self, nome_poco: str, target_date: "pd.Timestamp | str | None" = None
    ) -> "dict | None":
        """
        Identifica a sonda ativa no poço em uma data específica.

        Se target_date for None, retorna a vinculação mais recente.

        Returns:
            dict com 'sonda', 'inicio', 'fim', 'tipo_evento',
            'air_gap_m' (float ou None), 'datum_elevacao_m' (float ou None)
            — ou None se não encontrada.
        """
        df = self.get_vinculacao_sonda(nome_poco)
        if df.empty:
            return None

        # Garantir colunas de data como Timestamp
        for col in ("DT_INICIO_VINCULACAO", "DT_FIM_VINCULACAO"):
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors="coerce")

        if target_date is None:
            # Última vinculação (mais recente)
            row = df.iloc[-1]
        else:
            target = pd.Timestamp(target_date)
            # Filtrar: inicio <= target AND (fim >= target OR fim é NaT)
            mask = (
                df["DT_INICIO_VINCULACAO"].notna()
                & (df["DT_INICIO_VINCULACAO"] <= target)
                & (
                    df["DT_FIM_VINCULACAO"].isna()
                    | (df["DT_FIM_VINCULACAO"] >= target)
                )
            )
            matches = df.loc[mask]
            if matches.empty:
                logger.warning(
                    "[VINCULACAO] Nenhuma sonda encontrada para '%s' em %s",
                    nome_poco, target,
                )
                return None
            row = matches.iloc[-1]  # mais recente entre as válidas

        sonda_name = str(row.get("NM_SONDA", "")).strip() or None

        air_gap = row.get("MD_AIR_GAP")
        air_gap_m = float(air_gap) if pd.notna(air_gap) else None

        datum = row.get("MD_DATUM_ELEVACAO")
        datum_m = float(datum) if pd.notna(datum) else None

        result = {
            "sonda": sonda_name,
            "inicio": row.get("DT_INICIO_VINCULACAO"),
            "fim": row.get("DT_FIM_VINCULACAO"),
            "tipo_evento": str(row.get("TX_TIPO_EVENTO", "")).strip() or None,
            "air_gap_m": air_gap_m,
            "datum_elevacao_m": datum_m,
        }
        logger.info(
            "[VINCULACAO] Sonda ativa em %s: '%s' (%s), AG=%.1f m, início=%s, fim=%s",
            target_date or "(última)",
            result["sonda"],
            result["tipo_evento"],
            air_gap_m or 0.0,
            result["inicio"],
            result["fim"],
        )
        return result



# ======================================================================
# CLI rápido para teste
# ======================================================================
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Baixar geometria/direcional do Databricks")
    parser.add_argument("--host", required=True, help="server_hostname (ex: workspace.azuredatabricks.net)")
    parser.add_argument("--path", required=True, help="http_path do warehouse")
    parser.add_argument("--poco", required=True, help="Nome do poço (NM_POCO)")
    parser.add_argument("--save-csv", action="store_true", help="Salvar CSVs localmente")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    loader = DatabricksWellLoader(
        server_hostname=args.host,
        http_path=args.path,
    )

    df_dir = loader.get_direcional(args.poco)
    print(f"\n=== Direcional ({len(df_dir)} pontos) ===")
    print(df_dir[["MD_PROFUNDIDADE_MEDIDA", "MD_INCLINACAO", "MD_AZIMUTE",
                   "MD_PROFUNDIDADE_VERTICAL", "MD_DOGLEG_SEVERITY"]].to_string(index=False))

    df_rev = loader.get_revestimento(args.poco)
    print(f"\n=== Revestimento ({len(df_rev)} componentes) ===")
    if not df_rev.empty:
        cols = ["NM_ASSEMBLY", "NM_COMPONENTE", "MD_OD_COMPONENTE", "ID_BODY",
                "MD_TOP", "MD_BASE", "MD_SAPATA"]
        print(df_rev[[c for c in cols if c in df_rev.columns]].to_string(index=False))

    df_fase = loader.get_fase(args.poco)
    print(f"\n=== Fases ({len(df_fase)} fases) ===")
    if not df_fase.empty:
        cols = ["NR_FASE", "MD_DIAMETRO_FASE", "MD_PROF_TOPO_FASE",
                "MD_PROF_BASE_FASE", "MD_DIAMETRO_EXTERNO", "TX_MPD"]
        print(df_fase[[c for c in cols if c in df_fase.columns]].to_string(index=False))

    if args.save_csv:
        safe_name = args.poco.replace(" ", "_").replace("/", "_")
        df_dir.to_csv(f"direcional_{safe_name}.csv", index=False)
        df_rev.to_csv(f"revestimento_{safe_name}.csv", index=False)
        df_fase.to_csv(f"fase_{safe_name}.csv", index=False)
        print(f"\nCSVs salvos.")

    # Fluidos
    df_flu = loader.get_fluidos(args.poco)
    print(f"\n=== Fluidos ({len(df_flu)} registros) ===")
    if not df_flu.empty:
        # Helper: resolve column name from aliases (case-insensitive)
        def _col(df, *aliases):
            cols_up = {c.upper(): c for c in df.columns}
            for a in aliases:
                if a in df.columns:
                    return a
                real = cols_up.get(a.upper())
                if real:
                    return real
            return None

        fann_col = _col(df_flu, "MD_RPM_600")
        date_col = _col(df_flu, "DT_COLETA", "DT_DATA", "DT_BOLETIM")
        mw_col = _col(df_flu, "MD_DENSIDADE", "MD_PESO_FLUIDO")
        vp_col = _col(df_flu, "MD_VISCOSIDADE_PLASTICA", "MD_VIS_PLASTICA")
        le_col = _col(df_flu, "MD_LIM_ESCOAMENTO", "MD_LIMITE_ESCOAMENTO")
        g10s_col = _col(df_flu, "MD_GELS_10_SEC", "MD_GEL_INICIAL")
        g10m_col = _col(df_flu, "MD_GELS_10_MIN", "MD_GEL_10MIN")
        g30m_col = _col(df_flu, "MD_GELS_30_MIN", "MD_GEL_30MIN")

        # Filter to records with Fann readings
        with_fann = df_flu.dropna(subset=[fann_col]) if fann_col else df_flu
        if not with_fann.empty and date_col:
            last = with_fann.sort_values(date_col).iloc[-1]
            print(f"  Ultima leitura (fase {last.get('NR_FASE')}, {last.get(date_col)}):")
            print(f"    Densidade: {last.get(mw_col) if mw_col else '?'} ppg")
            print(f"    VP: {last.get(vp_col) if vp_col else '?'} cP, "
                  f"LE: {last.get(le_col) if le_col else '?'} lbf/100ft2")
            print(f"    Gels: 10s={last.get(g10s_col) if g10s_col else '?'}, "
                  f"10min={last.get(g10m_col) if g10m_col else '?'}, "
                  f"30min={last.get(g30m_col) if g30m_col else '?'}")
            r3 = _col(df_flu, "MD_RPM_3")
            r6 = _col(df_flu, "MD_RPM_6")
            r100 = _col(df_flu, "MD_RPM_100")
            r200 = _col(df_flu, "MD_RPM_200")
            r300 = _col(df_flu, "MD_RPM_300")
            print(f"    Fann: 3={last.get(r3) if r3 else '?'}, "
                  f"6={last.get(r6) if r6 else '?'}, "
                  f"100={last.get(r100) if r100 else '?'}, "
                  f"200={last.get(r200) if r200 else '?'}, "
                  f"300={last.get(r300) if r300 else '?'}, "
                  f"600={last.get(fann_col) if fann_col else '?'}")

    # Info do poço
    info = loader.get_info_poco(args.poco)
    if info:
        print(f"\n=== Info do poço ===")
        print(f"  Sonda: {info.get('NM_SONDA_REFERENCIA')}")
        print(f"  Bacia: {info.get('NM_BACIA')}")
        print(f"  Campo: {info.get('NM_COMPLETO_CAMPO')}")
        print(f"  LDA: {info.get('MD_LAMINA_DAGUA')} m")
        print(f"  Pré-sal: {info.get('IN_PRE_SAL')}")

    wg, *_ = loader.build_well_geometry(args.poco)
    print(f"\nWellGeometry: {wg}")
    print("\nSegmentos:")
    for s in wg.segments_m_top_to_bottom():
        print(f"  {s['name']:20s}  {s['length_m']:8.1f} m  "
              f"hole={s['hole_d_in']:.2f}\"  pipe={s['pipe_od_in']:.3f}\"")
