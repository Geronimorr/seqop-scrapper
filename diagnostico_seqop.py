r"""
Script de diagnóstico – coleta HTML dos elementos da página Arquivadas do SEQOP
para calibrar os seletores do scraper.

Uso: C:\SharedPython\venv\Scripts\python.exe diagnostico_seqop.py
"""
import subprocess, sys, time, os
from pathlib import Path

_SHARED_PYTHON = Path(r"C:\SharedPython\venv\Scripts\python.exe")
if _SHARED_PYTHON.exists() and Path(sys.executable).resolve() != _SHARED_PYTHON.resolve():
    result = subprocess.run([str(_SHARED_PYTHON)] + sys.argv, check=False)
    sys.exit(result.returncode)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import WebDriverException

SCRIPT_DIR = Path(__file__).resolve().parent
DEBUGGING_PORT = 9222
SAIDA_DIAG = SCRIPT_DIR / "diagnostico_saida.txt"

# Redirecionar print para arquivo também
import io

class Tee:
    """Escreve simultaneamente no terminal e num arquivo."""
    def __init__(self, *files):
        self.files = files
    def write(self, data):
        for f in self.files:
            f.write(data)
            f.flush()
    def flush(self):
        for f in self.files:
            f.flush()

_log_file = open(SAIDA_DIAG, "w", encoding="utf-8")
sys.stdout = Tee(sys.__stdout__, _log_file)

def criar_driver():
    # Tentar conectar ao Edge existente
    try:
        options = EdgeOptions()
        options.debugger_address = f"127.0.0.1:{DEBUGGING_PORT}"
        return webdriver.Edge(options=options)
    except WebDriverException:
        pass

    # Abrir novo Edge com perfil dedicado
    options = EdgeOptions()
    scraper_profile = Path(os.environ.get("LOCALAPPDATA", "")) / "SeqopScraper_Edge"
    scraper_profile.mkdir(parents=True, exist_ok=True)
    options.add_argument(f"--user-data-dir={scraper_profile}")
    options.add_argument("--profile-directory=Default")
    options.add_argument("--start-maximized")
    options.add_argument(f"--remote-debugging-port={DEBUGGING_PORT}")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    return webdriver.Edge(options=options)

print("Abrindo Edge...")
driver = criar_driver()

print(f"URL atual: {driver.current_url}")
print()

# Aguardar até que o usuário esteja na página de Arquivadas
while True:
    print("=" * 60)
    print("INSTRUÇÃO: No navegador que ABRIU (não no seu Edge pessoal),")
    print("  1. Faça login se necessário")
    print("  2. Clique em 'Sequências Arquivadas' no menu lateral")
    print("  3. Aguarde a tabela carregar")
    print("  4. Volte aqui e pressione Enter")
    print("=" * 60)
    input("Pressione Enter quando estiver na página de Arquivadas...")
    
    url = driver.current_url.lower()
    print(f"\nURL atual: {driver.current_url}")
    
    if "arquivadas" in url:
        print("✓ Página de Arquivadas confirmada!")
        break
    else:
        print(f"✗ Ainda NÃO está na página de Arquivadas.")
        print(f"  URL detectada: {driver.current_url}")
        print(f"  Tente novamente.\n")

print()
print(f"URL: {driver.current_url}")
print()

# ── Coletar HTML da sidebar ─────────────────────────────────────────────
print("=" * 80)
print("1. SIDEBAR (menu lateral)")
print("=" * 80)
try:
    sidebar_els = driver.find_elements(By.CSS_SELECTOR, 
        "nav, [class*='sidebar'], [class*='sidenav'], [class*='menu'], "
        "[class*='nav-'], aside, mat-sidenav")
    if not sidebar_els:
        # Fallback: pegar o primeiro elemento à esquerda
        sidebar_els = driver.find_elements(By.XPATH, 
            "//*[contains(text(),'Arquivadas')]/ancestor::*[position()<=3]")
    for i, el in enumerate(sidebar_els[:3]):
        print(f"\n--- Sidebar elemento {i} ({el.tag_name}, class='{el.get_attribute('class')}') ---")
        html = el.get_attribute("outerHTML")
        print(html[:2000])
except Exception as e:
    print(f"Erro: {e}")

# ── Coletar HTML dos filtros ────────────────────────────────────────────
print()
print("=" * 80)
print("2. FILTROS (campos Sonda, Poço, Polo, Título, botões)")
print("=" * 80)
try:
    # Todos os inputs visíveis
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for i, inp in enumerate(inputs):
        try:
            if inp.is_displayed():
                html = inp.get_attribute("outerHTML")
                parent_html = driver.execute_script(
                    "return arguments[0].parentElement.outerHTML;", inp)
                print(f"\n--- Input {i}: ---")
                print(f"  HTML: {html[:500]}")
                print(f"  Parent: {parent_html[:500]}")
        except:
            pass

    # Botões visíveis
    print("\n--- BOTÕES ---")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for i, btn in enumerate(buttons):
        try:
            if btn.is_displayed():
                html = btn.get_attribute("outerHTML")
                print(f"\n  Botão {i}: {html[:500]}")
        except:
            pass
except Exception as e:
    print(f"Erro: {e}")

# ── Coletar HTML da tabela ──────────────────────────────────────────────
print()
print("=" * 80)
print("3. TABELA (primeira linha de dados + cabeçalho)")
print("=" * 80)
try:
    # Cabeçalho
    ths = driver.find_elements(By.CSS_SELECTOR, "table th, table thead td")
    colunas = [th.text.strip() for th in ths if th.is_displayed()]
    print(f"\nColunas ({len(colunas)}): {colunas}")

    # Primeira linha de dados
    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    if rows:
        primeira = rows[0]
        print(f"\n--- 1ª linha (outerHTML): ---")
        html = primeira.get_attribute("outerHTML")
        print(html[:3000])

        # Coluna Ações especificamente
        tds = primeira.find_elements(By.TAG_NAME, "td")
        if tds:
            ultima = tds[-1]
            print(f"\n--- Coluna Ações (última TD, outerHTML): ---")
            print(ultima.get_attribute("outerHTML")[:1000])
    else:
        print("Nenhuma linha encontrada na tabela.")
except Exception as e:
    print(f"Erro: {e}")

# ── Coletar HTML da paginação ───────────────────────────────────────────
print()
print("=" * 80)
print("4. PAGINAÇÃO")
print("=" * 80)
try:
    pag_els = driver.find_elements(By.CSS_SELECTOR,
        "[class*='pagination'], ngb-pagination, ul.pagination, nav[aria-label*='pagination']")
    if not pag_els:
        pag_els = driver.find_elements(By.XPATH, 
            "//*[contains(text(),'›') or contains(text(),'»')]/..")
    for i, el in enumerate(pag_els[:3]):
        html = el.get_attribute("outerHTML")
        print(f"\n--- Paginação {i} ({el.tag_name}): ---")
        print(html[:2000])
except Exception as e:
    print(f"Erro: {e}")

print()
print("=" * 80)
print("DIAGNÓSTICO COMPLETO")
print("=" * 80)
print("Copie a saída acima e compartilhe comigo.")
print()
input("Pressione Enter para fechar...")
driver.quit()
