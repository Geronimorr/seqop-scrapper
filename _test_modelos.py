import requests, json, time, re, sys
import urllib3
urllib3.disable_warnings()

BASE = "https://apid.petrobras.com.br/ia/generativos/v1/litellm-chat-petrobras/litellm"
URL = BASE + "/engines/{model}/chat/completions"
H = {"api-key": "b320f1f58c9743e9a74048ce64717c89", "Content-Type": "application/json"}

# Prompt tecnico neutro (evita guardrail)
MSG_JSON = [
    {"role": "system", "content": "Voce e um especialista em perfuracao MPD. Responda SOMENTE em JSON valido."},
    {"role": "user", "content": (
        'Extraia pontos de verificacao deste comentario MPD:\n'
        '"Recomendo inserir fluxograma de controle de poco com MPD. '
        'Testar vedacao do SSA com 600 gpm e contrapressao de 700 a 750 psi. '
        'Monitorar poco pelo trip tank."\n\n'
        'JSON: {"pontos": [{"item": "...", "criticidade": "ALTA/MEDIA/BAIXA"}]}'
    )},
]

MODELOS = [
    "gpt-5.2", "gpt-5.1", "gpt-5", "gpt-5-mini",
    "gpt-4.1", "gpt-4.1-mini", "gpt-4o",
    "o4-mini", "o3", "o3-mini",
    "claude-sonnet-4-6", "claude-sonnet-4-5",
    "claude-opus-4-1", "claude-opus-4",
    "claude-sonnet-4", "claude-3-7-sonnet",
    "claude-haiku-4-5", "claude-4-5-haiku", "claude-3-5-haiku",
    "deepseek-r1-v1",
    "llama4-maverick-17b-instruct-v1", "llama4-scout-17b-instruct-v1",
    "qwen3-32b-v1",
    "mistral-large-2402-v1",
]

res = []
print(f"Testando {len(MODELOS)} modelos (apenas prompt JSON tecnico)...\n")
sys.stdout.flush()

for m in MODELOS:
    url = URL.replace("{model}", m)
    try:
        t0 = time.time()
        r = requests.post(url, headers=H, json={"messages": MSG_JSON, "max_tokens": 400, "temperature": 0.1}, timeout=60, verify=False)
        lat = time.time() - t0

        if r.status_code != 200:
            print(f"  FALHA  {m:42s} HTTP {r.status_code}")
            sys.stdout.flush()
            continue

        d = r.json()
        txt = d.get("choices", [{}])[0].get("message", {}).get("content", "")
        backend = d.get("model", "?")
        tok = d.get("usage", {})
        pt = tok.get("prompt_tokens", 0)
        ct = tok.get("completion_tokens", 0)

        # Classificar qualidade
        qual = "NAO_JSON"
        np_ = 0
        # Tentar parse direto
        try:
            p = json.loads(txt)
            np_ = len(p.get("pontos", []))
            qual = f"JSON_OK({np_}p)"
        except:
            # Tentar extrair JSON de dentro do texto
            match = re.search(r'\{[^{}]*"pontos"\s*:\s*\[.*?\]\s*\}', txt, re.DOTALL)
            if match:
                try:
                    p = json.loads(match.group())
                    np_ = len(p.get("pontos", []))
                    qual = f"JSON_EXTR({np_}p)"
                except:
                    qual = "JSON_PARCIAL"
            elif "guardrail" in txt.lower() or "violam" in txt.lower() or "cannot" in txt.lower():
                qual = "GUARDRAIL"
            elif "{" in txt:
                qual = "JSON_PARCIAL"

        print(f"  OK     {m:42s} {lat:5.1f}s  pt={pt:>4} ct={ct:>4}  {qual:18s}  {backend}")
        sys.stdout.flush()
        res.append({"modelo": m, "backend": backend, "lat": round(lat,1), "qual": qual, "pontos": np_, "pt": pt, "ct": ct})
    except requests.exceptions.Timeout:
        print(f"  TIMEOUT {m}")
        sys.stdout.flush()
    except Exception as e:
        print(f"  ERRO   {m}: {str(e)[:60]}")
        sys.stdout.flush()

# Ranking
print("\n" + "=" * 130)
print(f"{'#':>2} {'Modelo':<42} {'Lat':>6} {'Qual':<18} {'Pts':>4} {'TokP':>5} {'TokC':>5} {'Backend'}")
print("-" * 130)
for i, r in enumerate(sorted(res, key=lambda x: (-x["pontos"], x["lat"])), 1):
    print(f"{i:>2} {r['modelo']:<42} {r['lat']:>5.1f}s {r['qual']:<18} {r['pontos']:>4} {r['pt']:>5} {r['ct']:>5} {r['backend']}")

# Salvar JSON
with open("_resultado_benchmark.json", "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=2)
print(f"\nSalvo em _resultado_benchmark.json ({len(res)} modelos testados)")
