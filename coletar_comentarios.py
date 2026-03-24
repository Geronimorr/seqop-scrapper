"""
Coletor de Comentários SEQOP – Coleta TODOS os comentários de TODAS as URLs
============================================================================
Lê as URLs do resultado_aprovacoes_mpd.xlsx, visita cada página via Selenium,
extrai TODOS os comentários (não só MPD), e salva em comentarios_mpd.json.

Funcionalidades:
  - Coleta incremental: pula URLs já coletadas
  - Salva progresso a cada 10 URLs
  - Relatório final com estatísticas
  - Reconecta ao Edge existente na porta 9222

Uso:
    # Pré-requisito: abrir Edge com debugging port
    msedge.exe --remote-debugging-port=9222

    # Depois:
    C:\\SharedPython\\venv\\Scripts\\python.exe coletar_comentarios.py
    C:\\SharedPython\\venv\\Scripts\\python.exe coletar_comentarios.py --max-urls 50   # teste com 50
    C:\\SharedPython\\venv\\Scripts\\python.exe coletar_comentarios.py --reset          # recomeçar do zero
"""

# ── Re-launch com o venv compartilhado ──────────────────────────────────────
import subprocess
import sys
from pathlib import Path

_SHARED_PYTHON = Path(r"C:\SharedPython\venv\Scripts\python.exe")
if _SHARED_PYTHON.exists() and Path(sys.executable).resolve() != _SHARED_PYTHON.resolve():
    print(f"[LAUNCH] Relançando com {_SHARED_PYTHON}")
    result = subprocess.run([str(_SHARED_PYTHON)] + sys.argv, check=False)
    sys.exit(result.returncode)

# ── Imports ─────────────────────────────────────────────────────────────────
import argparse
import json
import logging
import os
import re
import time
import io
from datetime import datetime

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    WebDriverException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)

# ── Configuração ────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
ENTRADA_XLSX = SCRIPT_DIR / "resultado_aprovacoes_mpd.xlsx"
SAIDA_JSON = SCRIPT_DIR / "comentarios_mpd.json"
DEBUGGING_PORT = 9222

# ── Logging ─────────────────────────────────────────────────────────────────
log = logging.getLogger("coletar_comentarios")
log.setLevel(logging.INFO)

_fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

# Console handler com UTF-8
_ch = logging.StreamHandler(
    io.open(sys.stdout.fileno(), mode='w', encoding='utf-8', closefd=False)
)
_ch.setFormatter(_fmt)
log.addHandler(_ch)

# File handler
_fh = logging.FileHandler(SCRIPT_DIR / "coletar_comentarios.log", encoding="utf-8")
_fh.setFormatter(_fmt)
log.addHandler(_fh)


# ── Driver ──────────────────────────────────────────────────────────────────
def criar_driver():
    """Conecta ao Edge existente ou abre nova instância."""
    try:
        log.info(f"Conectando ao Edge na porta {DEBUGGING_PORT}...")
        opts = EdgeOptions()
        opts.debugger_address = f"127.0.0.1:{DEBUGGING_PORT}"
        d = webdriver.Edge(options=opts)
        log.info("Conectado ao Edge existente.")
        return d
    except WebDriverException:
        log.info("Abrindo nova instância do Edge...")

    opts = EdgeOptions()
    profile = Path(os.environ.get("LOCALAPPDATA", "")) / "SeqopScraper_Edge"
    profile.mkdir(parents=True, exist_ok=True)
    opts.add_argument(f"--user-data-dir={profile}")
    opts.add_argument("--profile-directory=Default")
    opts.add_argument("--start-maximized")
    opts.add_argument(f"--remote-debugging-port={DEBUGGING_PORT}")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    d = webdriver.Edge(options=opts)
    log.info("Edge aberto (perfil dedicado).")
    return d


def aguardar_login(driver):
    """Aguarda o usuário fazer login no CSD."""
    driver.get("https://csdpocos.petrobras.com.br/seqop")
    time.sleep(3)

    menus = driver.find_elements(By.CSS_SELECTOR, "aside.menu")
    if menus:
        log.info("Login detectado ✓")
        return

    log.info("⏳ Aguardando login manual no CSD Poços...")
    log.info("   Faça login no navegador e aguarde.")
    for _ in range(120):  # 10 min timeout
        time.sleep(5)
        menus = driver.find_elements(By.CSS_SELECTOR, "aside.menu")
        if menus:
            log.info("Login detectado ✓")
            return

    log.warning("Timeout aguardando login. Continuando mesmo assim...")


# ── Extração de Comentários ─────────────────────────────────────────────────
def extrair_comentarios_pagina(driver) -> list[dict]:
    """Extrai TODOS os comentários da página de detalhe da SEQOP."""
    comentarios = []

    try:
        grupos = driver.find_elements(By.CSS_SELECTOR, "div.grupoComentario")
        for grupo in grupos:
            try:
                # Texto do comentário principal
                texto = ""
                try:
                    card = grupo.find_element(By.CSS_SELECTOR, "div.card-text")
                    texto = card.text.strip()
                except Exception:
                    pass

                # Autor e tipo (CSD-MPD, CSD-SMAB, Fiscal, etc.)
                autor = ""
                tipo_csd = ""
                versao = ""
                try:
                    autor_div = grupo.find_element(
                        By.CSS_SELECTOR, "div.emLinhaAutor.autor-versao"
                    )
                    spans = autor_div.find_elements(By.TAG_NAME, "span")
                    if len(spans) >= 1:
                        nome_raw = spans[0].text.strip()
                        # Remove "há X dias/meses" suffix
                        autor = re.sub(
                            r"\s+h[aá]\s+\d+\s+\w+$", "", nome_raw,
                            flags=re.IGNORECASE,
                        ).strip()
                    if len(spans) >= 2:
                        info = spans[1].text.strip()  # "CSD-MPD - Versão: 2"
                        m_tipo = re.match(
                            r"(CSD-\w+|Fiscal)\s*-\s*Vers[aã]o:\s*(\d+)",
                            info, re.IGNORECASE
                        )
                        if m_tipo:
                            tipo_csd = m_tipo.group(1)
                            versao = m_tipo.group(2)
                        else:
                            tipo_csd = info
                except Exception:
                    pass

                # Respostas ao comentário
                respostas = []
                try:
                    replies = grupo.find_elements(By.CSS_SELECTOR, "div.replyComments")
                    for reply in replies:
                        try:
                            reply_text = ""
                            try:
                                rc = reply.find_element(By.CSS_SELECTOR, "div.card-text")
                                reply_text = rc.text.strip()
                            except Exception:
                                pass
                            reply_autor = ""
                            try:
                                ra = reply.find_element(
                                    By.CSS_SELECTOR, "div.emLinhaAutor.autor-versao"
                                )
                                rs = ra.find_elements(By.TAG_NAME, "span")
                                if rs:
                                    reply_autor = re.sub(
                                        r"\s+h[aá]\s+\d+\s+\w+$", "",
                                        rs[0].text.strip(), flags=re.IGNORECASE,
                                    ).strip()
                            except Exception:
                                pass
                            if reply_text:
                                respostas.append({
                                    "autor": reply_autor,
                                    "texto": reply_text,
                                })
                        except Exception:
                            continue
                except Exception:
                    pass

                if texto or respostas:
                    comentarios.append({
                        "autor": autor,
                        "tipo_csd": tipo_csd,
                        "versao": versao,
                        "texto": texto,
                        "respostas": respostas,
                    })

            except (NoSuchElementException, StaleElementReferenceException):
                continue

    except Exception as e:
        log.warning(f"  Erro ao extrair comentários: {e}")

    return comentarios


# ── Carregar URLs do Excel ──────────────────────────────────────────────────
def carregar_urls_excel() -> list[dict]:
    """Lê URLs únicas do resultado_aprovacoes_mpd.xlsx."""
    if not ENTRADA_XLSX.exists():
        log.error(f"Arquivo não encontrado: {ENTRADA_XLSX}")
        return []

    df = pd.read_excel(ENTRADA_XLSX, engine="openpyxl")
    log.info(f"Excel carregado: {len(df)} linhas")

    urls_unicas = []
    urls_vistas = set()
    for _, row in df.iterrows():
        url = str(row.get("URL Fonte", ""))
        if url and url.startswith("http") and url not in urls_vistas:
            urls_vistas.add(url)
            urls_unicas.append({
                "url": url,
                "poco": str(row.get("Poço", "")),
                "titulo": str(row.get("Título", "")),
                "seq_id": str(row.get("Seq ID", "")),
            })

    log.info(f"URLs únicas: {len(urls_unicas)}")
    return urls_unicas


def carregar_existentes() -> list[dict]:
    """Carrega comentários já coletados."""
    if SAIDA_JSON.exists():
        try:
            with open(SAIDA_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            log.warning(f"Erro lendo {SAIDA_JSON}: {e}")
    return []


def salvar_json(dados):
    """Salva dados em JSON."""
    with open(SAIDA_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


# ── Coleta Principal ────────────────────────────────────────────────────────
def coletar(max_urls: int = 0, reset: bool = False):
    """Coleta comentários de todas as URLs pendentes."""

    # Carregar URLs
    urls_todas = carregar_urls_excel()
    if not urls_todas:
        return

    # Carregar existentes (ou resetar)
    if reset:
        dados_existentes = []
        log.info("🔄 Reset: ignorando dados existentes")
    else:
        dados_existentes = carregar_existentes()
        log.info(f"Comentários já coletados: {len(dados_existentes)} SEQOPs")

    # Filtrar URLs pendentes
    urls_coletadas = {d.get("url", "") for d in dados_existentes}
    urls_pendentes = [u for u in urls_todas if u["url"] not in urls_coletadas]

    if max_urls > 0:
        urls_pendentes = urls_pendentes[:max_urls]

    log.info(f"URLs pendentes: {len(urls_pendentes)} de {len(urls_todas)}")

    if not urls_pendentes:
        log.info("✅ Nenhuma URL pendente! Todas já foram coletadas.")
        _imprimir_resumo(dados_existentes)
        return

    # Conectar ao Edge
    driver = criar_driver()
    aguardar_login(driver)
    time.sleep(2)

    # Coletar
    dados = list(dados_existentes)  # cópia
    erros = 0
    t_inicio = time.time()

    log.info("=" * 70)
    log.info(f"COLETA DE COMENTÁRIOS – {len(urls_pendentes)} URLs")
    log.info("=" * 70)

    for idx, info in enumerate(urls_pendentes, 1):
        url = info["url"]
        poco = info["poco"]
        titulo = info["titulo"][:50]

        log.info(f"[{idx}/{len(urls_pendentes)}] {poco} – {titulo}")

        try:
            driver.get(url)

            # Aguardar carregamento
            try:
                WebDriverWait(driver, 15).until(
                    lambda d: d.execute_script("return document.readyState") == "complete"
                )
            except TimeoutException:
                pass

            # Aguardar conteúdo dinâmico (SPA Angular)
            time.sleep(2.5)

            # Tentar aguardar sidebar ou conteúdo
            try:
                WebDriverWait(driver, 8).until(
                    lambda d: d.find_elements(By.CSS_SELECTOR, "div.SideBar") or
                              d.find_elements(By.CSS_SELECTOR, "div.grupoComentario") or
                              d.find_elements(By.CSS_SELECTOR, "div.content")
                )
            except TimeoutException:
                pass

            time.sleep(0.5)

            # Extrair comentários
            comentarios = extrair_comentarios_pagina(driver)

            # Título da página (mais preciso)
            titulo_pagina = info["titulo"]
            try:
                h5s = driver.find_elements(By.CSS_SELECTOR, "div.SideBar h5")
                if len(h5s) >= 2:
                    t = h5s[1].text.strip()
                    if t:
                        titulo_pagina = t
            except Exception:
                pass

            n_mpd = sum(1 for c in comentarios if "MPD" in c.get("tipo_csd", "").upper())

            dados.append({
                "url": url,
                "poco": info["poco"],
                "titulo": titulo_pagina,
                "seq_id": info["seq_id"],
                "comentarios": comentarios,
                "conteudo_seqop": "",  # não coletamos conteúdo (muito grande)
                "comentarios_mpd": [c for c in comentarios if "MPD" in c.get("tipo_csd", "").upper()],
                "total_comentarios": len(comentarios),
                "total_mpd": n_mpd,
            })

            status = f"→ {len(comentarios)} comentários ({n_mpd} MPD)"
            if not comentarios:
                status = "→ sem comentários"
            log.info(f"    {status}")

        except Exception as e:
            erros += 1
            log.error(f"    ERRO: {e}")
            dados.append({
                "url": url,
                "poco": info["poco"],
                "titulo": info["titulo"],
                "seq_id": info["seq_id"],
                "comentarios": [],
                "conteudo_seqop": "",
                "comentarios_mpd": [],
                "total_comentarios": 0,
                "total_mpd": 0,
                "erro": str(e),
            })

        # Salvar progresso a cada 10 URLs
        if idx % 10 == 0:
            salvar_json(dados)
            elapsed = time.time() - t_inicio
            rate = idx / elapsed if elapsed > 0 else 0
            remaining = (len(urls_pendentes) - idx) / rate if rate > 0 else 0
            log.info(f"  📊 Progresso: {idx}/{len(urls_pendentes)} "
                     f"({idx*100//len(urls_pendentes)}%) "
                     f"| {elapsed:.0f}s | ETA: {remaining:.0f}s "
                     f"| Erros: {erros}")

    # Salvar final
    salvar_json(dados)
    elapsed = time.time() - t_inicio

    log.info("=" * 70)
    log.info(f"COLETA COMPLETA em {elapsed:.0f}s")
    log.info(f"  Novas URLs coletadas: {len(urls_pendentes)}")
    log.info(f"  Erros: {erros}")
    log.info("=" * 70)

    _imprimir_resumo(dados)


def _imprimir_resumo(dados: list[dict]):
    """Imprime resumo dos comentários coletados."""
    total_seqops = len(dados)
    total_com = sum(d.get("total_comentarios", 0) for d in dados)
    total_mpd = sum(d.get("total_mpd", 0) for d in dados)
    com_erros = sum(1 for d in dados if d.get("erro"))
    pocos = set(d.get("poco", "") for d in dados)
    seqops_com_mpd = sum(1 for d in dados if d.get("total_mpd", 0) > 0)
    seqops_com_comentarios = sum(1 for d in dados if d.get("total_comentarios", 0) > 0)

    # Tipos de CSD encontrados
    tipos_csd = {}
    for d in dados:
        for c in d.get("comentarios", []):
            tipo = c.get("tipo_csd", "?")
            tipos_csd[tipo] = tipos_csd.get(tipo, 0) + 1

    log.info("\n" + "=" * 70)
    log.info("RESUMO DOS COMENTÁRIOS COLETADOS")
    log.info("=" * 70)
    log.info(f"  SEQOPs total:           {total_seqops}")
    log.info(f"  SEQOPs com comentários: {seqops_com_comentarios}")
    log.info(f"  SEQOPs com CSD-MPD:     {seqops_com_mpd}")
    log.info(f"  SEQOPs com erro:        {com_erros}")
    log.info(f"  Poços:                  {len(pocos)}")
    log.info(f"  Comentários total:      {total_com}")
    log.info(f"  Comentários MPD:        {total_mpd}")
    log.info(f"")
    log.info(f"  Tipos de CSD:")
    for tipo, count in sorted(tipos_csd.items(), key=lambda x: -x[1]):
        log.info(f"    {tipo:20s}: {count}")
    log.info(f"")
    log.info(f"  Arquivo: {SAIDA_JSON}")
    log.info("=" * 70)


# ── Main ────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Coletor de comentários de SEQOPs para checklist MPD"
    )
    parser.add_argument("--max-urls", type=int, default=0,
                        help="Limite de URLs a coletar (0 = todas pendentes)")
    parser.add_argument("--reset", action="store_true",
                        help="Ignorar dados existentes e recomeçar do zero")
    parser.add_argument("--resumo", action="store_true",
                        help="Apenas mostrar resumo dos dados existentes")
    args = parser.parse_args()

    log.info("=" * 70)
    log.info("COLETOR DE COMENTÁRIOS SEQOP")
    log.info(f"Data/hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    log.info("=" * 70)

    if args.resumo:
        dados = carregar_existentes()
        if dados:
            _imprimir_resumo(dados)
        else:
            log.info("Nenhum dado existente.")
        return

    coletar(max_urls=args.max_urls, reset=args.reset)


if __name__ == "__main__":
    main()
