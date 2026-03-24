"""Teste: baixar 1 PDF extraindo cookies do Edge (sem debugging port)."""
import json, re, os
import requests, urllib3
urllib3.disable_warnings()

# Carregar 1 SEQOP de exemplo
with open("comentarios_mpd.json", "r", encoding="utf-8") as f:
    seqops = json.load(f)

item = seqops[0]
url_seqop = item["url"]
m = re.search(r'([a-f0-9]{24})', url_seqop)
mongo_id = m.group(1)
pdf_url = f"https://csdpocos.petrobras.com.br/seqop/api/file/pdf/{mongo_id}/name/doc/"
print(f"SEQOP: {item['titulo']}")
print(f"Mongo ID: {mongo_id}")
print(f"PDF URL: {pdf_url}")

# ── Estratégia 1: browser_cookie3 ──────────────────────────────────
session = requests.Session()
try:
    import browser_cookie3
    print("\nTentando browser_cookie3 (Edge)...")
    cj = browser_cookie3.edge(domain_name=".petrobras.com.br")
    session.cookies = cj
    n_cookies = len([c for c in cj])
    print(f"  Cookies extraídos: {n_cookies}")
except Exception as e:
    print(f"  browser_cookie3 falhou: {e}")

# ── Estratégia 2: NTLM (Windows Integrated Auth) ──────────────────
if not session.cookies:
    try:
        from requests_ntlm import HttpNtlmAuth
        user = os.environ.get("USERNAME", "")
        domain = os.environ.get("USERDOMAIN", "")
        print(f"\nTentando NTLM: {domain}\\{user}")
        session.auth = HttpNtlmAuth(f"{domain}\\{user}", "")
    except ImportError:
        print("  requests_ntlm não instalado")

# ── Download ──────────────────────────────────────────────────────
print(f"\nBaixando PDF...")
resp = session.get(pdf_url, timeout=30, verify=False)
print(f"Status: {resp.status_code}")
print(f"Content-Type: {resp.headers.get('content-type', '?')}")
print(f"Content-Length: {len(resp.content)} bytes")

if resp.status_code == 200 and len(resp.content) > 1000:
    ct = resp.headers.get('content-type', '')
    if 'pdf' in ct or resp.content[:5] == b'%PDF-':
        with open("_test.pdf", "wb") as f:
            f.write(resp.content)
        print("PDF salvo!")
        
        import fitz
        doc = fitz.open("_test.pdf")
        texto = ""
        for page in doc:
            texto += page.get_text()
        print(f"Texto: {len(texto)} chars, {doc.page_count} páginas")
        print(f"\n{'='*60}")
        print(texto[:800])
        doc.close()
    else:
        print(f"Resposta não é PDF. Primeiros bytes: {resp.content[:100]}")
elif resp.status_code == 200:
    print(f"Resposta muito pequena: {resp.text[:200]}")
else:
    print(f"Falha: {resp.text[:300]}")
