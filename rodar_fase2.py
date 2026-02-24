"""
Executa somente a Fase 2 do scraper, usando as sequências já coletadas
na Fase 1 (lidas do log ou hardcoded).
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
import re
import time
import logging

# Importar tudo do scraper principal
from scraper_seqop import (
    SequenciaMPD, AprovacaoMPD,
    criar_driver, aguardar_login, salvar_excel,
    fase2_extrair_historico,
    SCRIPT_DIR, SAIDA_XLSX, WAIT_TIMEOUT,
    log,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

# ── Parsear log para extrair sequências da Fase 1 ──────────────────────────

LOG_FILE = SCRIPT_DIR / "scraper_seqop.log"

# Formato do log:
# "  poco | seq_id | titulo(truncado) | url"
RE_LOG_LINE = re.compile(
    r"^\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2},\d+\s+\[INFO\]\s+"
    r"(\S.*?)\s+\|\s+(\S+)\s+\|\s+(.+?)\s+\|\s+(https://\S+)$"
)


def carregar_sequencias_do_log() -> list[SequenciaMPD]:
    """Lê o log e extrai as sequências listadas após 'FASE 1 COMPLETA'."""
    sequencias = []
    dentro_do_bloco = False

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if "FASE 1 COMPLETA:" in line:
                dentro_do_bloco = True
                continue
            if dentro_do_bloco:
                if "====" in line or "FASE 2" in line:
                    break  # fim do bloco
                m = RE_LOG_LINE.match(line.strip())
                if m:
                    poco, seq_id, titulo, url = (
                        m.group(1).strip(),
                        m.group(2).strip(),
                        m.group(3).strip(),
                        m.group(4).strip(),
                    )
                    sequencias.append(SequenciaMPD(
                        poco=poco, titulo=titulo,
                        versao_tabela="", publicado_em="",
                        url=url, seq_id=seq_id,
                    ))

    return sequencias


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    sequencias = carregar_sequencias_do_log()
    log.info(f"Carregadas {len(sequencias)} sequências do log da Fase 1")

    if not sequencias:
        log.error("Nenhuma sequência encontrada no log! Verifique o arquivo.")
        return

    for i, s in enumerate(sequencias[:5], 1):
        log.info(f"  Exemplo {i}: {s.poco} | {s.titulo[:50]} | {s.url}")

    driver = criar_driver()
    wait = WebDriverWait(driver, WAIT_TIMEOUT,
                         ignored_exceptions=[StaleElementReferenceException])

    aguardar_login(driver)

    todos_resultados: list[AprovacaoMPD] = []

    log.info("=" * 60)
    log.info(f"FASE 2 (standalone) – {len(sequencias)} sequências")
    log.info("=" * 60)

    for idx, seq in enumerate(sequencias, 1):
        log.info(f"[{idx}/{len(sequencias)}] {seq.poco} – {seq.titulo[:50]}")
        try:
            aprovacoes = fase2_extrair_historico(driver, wait, seq)
            todos_resultados.extend(aprovacoes)
        except Exception as e:
            log.error(f"Erro seq {seq.seq_id}: {e}", exc_info=True)
            todos_resultados.append(AprovacaoMPD(
                poco=seq.poco, seq_id=seq.seq_id, titulo=seq.titulo,
                versao=seq.versao_tabela, aprovado_por=f"(ERRO: {e})",
                aprovado_em="", fonte_url=seq.url,
            ))

        # Salvar progresso a cada 10
        if idx % 10 == 0 and todos_resultados:
            salvar_excel(todos_resultados)
            log.info(f"  Progresso: {len(todos_resultados)} aprovações salvas")

    if todos_resultados:
        salvar_excel(todos_resultados)

    log.info("=" * 60)
    log.info(f"FASE 2 COMPLETA: {len(todos_resultados)} aprovações → {SAIDA_XLSX}")
    log.info("=" * 60)

    try:
        input("\nPressione Enter para fechar o navegador...")
    except EOFError:
        pass
    driver.quit()


if __name__ == "__main__":
    main()
