"""Gera Excel + HTML a partir do JSON já salvo (sem re-chamar a IA)."""
import subprocess, sys
from pathlib import Path
_SHARED_PYTHON = Path(r"C:\SharedPython\venv\Scripts\python.exe")
if _SHARED_PYTHON.exists() and Path(sys.executable).resolve() != _SHARED_PYTHON.resolve():
    result = subprocess.run([str(_SHARED_PYTHON)] + sys.argv, check=False)
    sys.exit(result.returncode)

import json, io, logging
sys.stdout = io.open(sys.stdout.fileno(), mode='w', encoding='utf-8', closefd=False)

from gerar_checklist_combinado import (
    fase4_gerar_excel, fase4_gerar_html, log, COMBINADO_JSON
)

log.setLevel(logging.INFO)
if not log.handlers:
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    log.addHandler(h)

with open(COMBINADO_JSON, "r", encoding="utf-8") as f:
    checklist = json.load(f)

print(f"Carregado: {len(checklist.get('categorias',[]))} categorias, "
      f"{sum(len(c.get('itens',[])) for c in checklist.get('categorias',[]))} itens")

fase4_gerar_excel(checklist)
fase4_gerar_html(checklist)
print("Concluído!")
