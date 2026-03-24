"""
Fase A — Baixar PDFs das SEQOPs e extrair texto
================================================
Lê 'comentarios_mpd.json', baixa o PDF de cada SEQOP via API HTTP,
extrai texto com PyMuPDF e salva em 'seqops_texto_pdf.json'.

Não precisa de Selenium nem de Edge na porta 9222.
Usa autenticação automática da rede Petrobras.

Uso:
    python baixar_pdfs.py                # todas as SEQOPs
    python baixar_pdfs.py --max 5        # testar com 5
    python baixar_pdfs.py --force        # re-baixar já existentes
"""
import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import fitz  # PyMuPDF
import requests
import urllib3
urllib3.disable_warnings()

# ── Configuração ───────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
ENTRADA_JSON = SCRIPT_DIR / "comentarios_mpd.json"
SAIDA_JSON   = SCRIPT_DIR / "seqops_texto_pdf.json"
PDF_DIR      = SCRIPT_DIR / "pdfs"

BASE_PDF_URL = "https://csdpocos.petrobras.com.br/seqop/api/file/pdf/{mongo_id}/name/doc/"

# ── Funções ────────────────────────────────────────────────────────────────

def extrair_mongo_id(url: str) -> str | None:
    """Extrai o mongo ID (24 hex chars) da URL da SEQOP."""
    m = re.search(r'([a-f0-9]{24})', url)
    return m.group(1) if m else None


def baixar_pdf(session: requests.Session, mongo_id: str, dest: Path) -> bool:
    """Baixa o PDF e salva no disco. Retorna True se sucesso."""
    url = BASE_PDF_URL.format(mongo_id=mongo_id)
    try:
        resp = session.get(url, timeout=45, verify=False)
        if resp.status_code == 200 and len(resp.content) > 500:
            ct = resp.headers.get("content-type", "")
            if "pdf" in ct or resp.content[:5] == b"%PDF-":
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(resp.content)
                return True
        return False
    except Exception:
        return False


def extrair_texto_pdf(caminho: Path) -> str:
    """Extrai texto de um PDF com PyMuPDF."""
    try:
        doc = fitz.open(str(caminho))
        texto = ""
        for page in doc:
            texto += page.get_text()
        doc.close()
        return texto.strip()
    except Exception as e:
        return f"[ERRO EXTRAÇÃO: {e}]"


def main():
    parser = argparse.ArgumentParser(description="Baixar PDFs das SEQOPs")
    parser.add_argument("--max", type=int, default=0, help="Máximo de SEQOPs (0=todas)")
    parser.add_argument("--force", action="store_true", help="Re-baixar PDFs já existentes")
    args = parser.parse_args()

    # Carregar dados
    if not ENTRADA_JSON.exists():
        print(f"ERRO: {ENTRADA_JSON} não encontrado")
        sys.exit(1)

    with open(ENTRADA_JSON, "r", encoding="utf-8") as f:
        seqops = json.load(f)

    print(f"SEQOPs carregadas: {len(seqops)}")

    # Carregar resultados existentes
    resultados = {}
    if SAIDA_JSON.exists() and not args.force:
        with open(SAIDA_JSON, "r", encoding="utf-8") as f:
            existentes = json.load(f)
        resultados = {r["mongo_id"]: r for r in existentes if r.get("mongo_id")}
        print(f"Já processadas: {len(resultados)}")

    # Sessão HTTP (usa SSO automático da rede Petrobras)
    session = requests.Session()

    # Processar
    PDF_DIR.mkdir(exist_ok=True)
    processadas = 0
    erros = 0
    t0 = time.time()

    total = len(seqops) if args.max == 0 else min(args.max, len(seqops))

    for idx, item in enumerate(seqops[:total]):
        mongo_id = extrair_mongo_id(item.get("url", ""))
        if not mongo_id:
            erros += 1
            continue

        # Pular já processadas
        if mongo_id in resultados and not args.force:
            continue

        titulo = item.get("titulo", "?")[:60]
        poco = item.get("poco", "?")
        pdf_path = PDF_DIR / f"{mongo_id}.pdf"

        # Baixar PDF
        if not pdf_path.exists() or args.force:
            ok = baixar_pdf(session, mongo_id, pdf_path)
            if not ok:
                print(f"  [{idx+1}/{total}] FALHA  {poco} — {titulo}")
                erros += 1
                resultados[mongo_id] = {
                    "mongo_id": mongo_id,
                    "url": item.get("url", ""),
                    "poco": poco,
                    "titulo": item.get("titulo", ""),
                    "texto_pdf": "",
                    "n_paginas": 0,
                    "n_chars": 0,
                    "erro": "download_falhou",
                }
                continue

        # Extrair texto
        texto = extrair_texto_pdf(pdf_path)
        n_paginas = 0
        try:
            doc = fitz.open(str(pdf_path))
            n_paginas = doc.page_count
            doc.close()
        except:
            pass

        resultados[mongo_id] = {
            "mongo_id": mongo_id,
            "url": item.get("url", ""),
            "poco": poco,
            "titulo": item.get("titulo", ""),
            "seq_id": item.get("seq_id", ""),
            "texto_pdf": texto,
            "n_paginas": n_paginas,
            "n_chars": len(texto),
        }
        processadas += 1

        if processadas % 10 == 0 or processadas <= 3:
            elapsed = time.time() - t0
            rate = processadas / elapsed if elapsed > 0 else 0
            remaining = (total - idx - 1) / rate / 60 if rate > 0 else 0
            print(f"  [{idx+1}/{total}] OK  {n_paginas:>2}p {len(texto):>6}ch  "
                  f"{poco} — {titulo}  ({elapsed:.0f}s, ETA {remaining:.1f}min)")

        # Salvar progresso a cada 25
        if processadas % 25 == 0:
            _salvar(resultados)

    # Salvar final
    _salvar(resultados)
    elapsed = time.time() - t0

    # Estatísticas
    todos = list(resultados.values())
    com_texto = [r for r in todos if r.get("n_chars", 0) > 100]
    total_chars = sum(r.get("n_chars", 0) for r in todos)
    total_paginas = sum(r.get("n_paginas", 0) for r in todos)

    print(f"\n{'='*60}")
    print(f"DOWNLOAD COMPLETO em {elapsed:.0f}s")
    print(f"  Total processadas: {len(todos)}")
    print(f"  Com texto: {len(com_texto)}")
    print(f"  Erros: {erros}")
    print(f"  Total páginas: {total_paginas}")
    print(f"  Total caracteres: {total_chars:,}")
    print(f"  PDFs salvos em: {PDF_DIR}")
    print(f"  JSON salvo em: {SAIDA_JSON}")


def _salvar(resultados: dict):
    """Salva resultados em JSON."""
    dados = list(resultados.values())
    with open(SAIDA_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
