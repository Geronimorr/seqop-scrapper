"""
Teste da API de IA Generativa Petrobras (LiteLLM Chat Completions)
===================================================================
Testa conectividade, autenticação e formato de resposta.

Uso:
    python testar_api_ia.py
"""

import json
import requests
import sys

# ── Configuração ────────────────────────────────────────────────────────────

BASE_URL = "https://apid.petrobras.com.br/ia/generativos/v1/litellm-chat-petrobras/litellm"
ENGINE_URL = BASE_URL + "/engines/{model}/chat/completions"

PRIMARY_KEY = "b320f1f58c9743e9a74048ce64717c89"
SECONDARY_KEY = "60d1ced9cea44c20abf145b32755b0be"

# Modelos comuns para tentar (LiteLLM pode rotear para vários)
MODELOS_TENTAR = [
    "gpt-4o",
    "gpt-4",
    "gpt-4-turbo",
    "gpt-4o-mini",
    "gpt-35-turbo",
    "gpt-3.5-turbo",
    "llama-3",
    "claude-3",
]

MENSAGEM_TESTE = [
    {"role": "system", "content": "Você é um assistente útil. Responda em português de forma breve."},
    {"role": "user", "content": "Olá! Diga apenas: 'API funcionando!' e nada mais."},
]


def separador(texto=""):
    print(f"\n{'='*60}")
    if texto:
        print(f"  {texto}")
        print(f"{'='*60}")


def testar_endpoints_auxiliares(headers):
    """Testa endpoints auxiliares do LiteLLM para descobrir modelos disponíveis."""
    separador("TESTE 1: Descobrir modelos disponíveis")

    endpoints_modelos = [
        BASE_URL + "/models",
        BASE_URL + "/v1/models",
        BASE_URL + "/model/info",
    ]

    for url in endpoints_modelos:
        print(f"\n→ GET {url}")
        try:
            resp = requests.get(url, headers=headers, timeout=15, verify=True)
            print(f"  Status: {resp.status_code}")
            if resp.status_code == 200:
                data = resp.json()
                print(f"  Resposta: {json.dumps(data, indent=2, ensure_ascii=False)[:1500]}")
                # Extrair nomes de modelos
                if isinstance(data, dict) and "data" in data:
                    modelos = [m.get("id", m.get("model", "?")) for m in data["data"]]
                    print(f"\n  ★ Modelos encontrados: {modelos}")
                    return modelos
            else:
                print(f"  Corpo: {resp.text[:300]}")
        except requests.exceptions.SSLError as e:
            print(f"  ✗ Erro SSL: {e}")
            print("  → Tentando sem verificação SSL...")
            try:
                resp = requests.get(url, headers=headers, timeout=15, verify=False)
                print(f"  Status (no-verify): {resp.status_code}")
                if resp.status_code == 200:
                    data = resp.json()
                    print(f"  Resposta: {json.dumps(data, indent=2, ensure_ascii=False)[:1500]}")
                    if isinstance(data, dict) and "data" in data:
                        modelos = [m.get("id", m.get("model", "?")) for m in data["data"]]
                        print(f"\n  ★ Modelos encontrados: {modelos}")
                        return modelos
                else:
                    print(f"  Corpo: {resp.text[:300]}")
            except Exception as e2:
                print(f"  ✗ Erro: {e2}")
        except Exception as e:
            print(f"  ✗ Erro: {e}")

    return None


def testar_chat_completion(headers, modelo, verify_ssl=True):
    """Testa o endpoint de chat completions com um modelo específico."""
    url = ENGINE_URL.replace("{model}", modelo)
    print(f"\n→ POST {url}")

    payload = {
        "messages": MENSAGEM_TESTE,
        "max_tokens": 50,
        "temperature": 0.1,
    }

    try:
        resp = requests.post(
            url, headers=headers, json=payload,
            timeout=30, verify=verify_ssl,
        )
        print(f"  Status: {resp.status_code}")

        if resp.status_code == 200:
            data = resp.json()
            # Extrair resposta
            choices = data.get("choices", [])
            if choices:
                msg = choices[0].get("message", {}).get("content", "(vazio)")
                print(f"  ★ Resposta do modelo: {msg}")
            else:
                print(f"  Resposta completa: {json.dumps(data, indent=2, ensure_ascii=False)[:800]}")

            # Mostrar uso de tokens
            usage = data.get("usage", {})
            if usage:
                print(f"  Tokens: prompt={usage.get('prompt_tokens')}, "
                      f"completion={usage.get('completion_tokens')}, "
                      f"total={usage.get('total_tokens')}")

            print(f"\n  ✓ SUCESSO com modelo '{modelo}'!")
            return True
        else:
            print(f"  Corpo: {resp.text[:500]}")
            return False

    except requests.exceptions.SSLError:
        if verify_ssl:
            print(f"  ⚠ Erro SSL, tentando sem verificação...")
            return testar_chat_completion(headers, modelo, verify_ssl=False)
        print(f"  ✗ Erro SSL persistente")
        return False
    except Exception as e:
        print(f"  ✗ Erro: {e}")
        return False


def testar_endpoint_v1(headers, modelo, verify_ssl=True):
    """Testa formato alternativo /v1/chat/completions com model no body."""
    url = BASE_URL + "/v1/chat/completions"
    print(f"\n→ POST {url}  (model={modelo} no body)")

    payload = {
        "model": modelo,
        "messages": MENSAGEM_TESTE,
        "max_tokens": 50,
        "temperature": 0.1,
    }

    try:
        resp = requests.post(
            url, headers=headers, json=payload,
            timeout=30, verify=verify_ssl,
        )
        print(f"  Status: {resp.status_code}")

        if resp.status_code == 200:
            data = resp.json()
            choices = data.get("choices", [])
            if choices:
                msg = choices[0].get("message", {}).get("content", "(vazio)")
                print(f"  ★ Resposta do modelo: {msg}")
            else:
                print(f"  Resposta: {json.dumps(data, indent=2, ensure_ascii=False)[:800]}")

            usage = data.get("usage", {})
            if usage:
                print(f"  Tokens: prompt={usage.get('prompt_tokens')}, "
                      f"completion={usage.get('completion_tokens')}, "
                      f"total={usage.get('total_tokens')}")

            print(f"\n  ✓ SUCESSO com /v1/chat/completions + model='{modelo}'!")
            return True
        else:
            print(f"  Corpo: {resp.text[:500]}")
            return False

    except requests.exceptions.SSLError:
        if verify_ssl:
            print(f"  ⚠ Erro SSL, tentando sem verificação...")
            return testar_endpoint_v1(headers, modelo, verify_ssl=False)
        return False
    except Exception as e:
        print(f"  ✗ Erro: {e}")
        return False


def testar_combinacao(header_dict, modelo, label, verify_ssl=False):
    """Testa uma combinação header+modelo e retorna True se 200."""
    url = ENGINE_URL.replace("{model}", modelo)
    payload = {
        "messages": MENSAGEM_TESTE,
        "max_tokens": 50,
        "temperature": 0.1,
    }
    try:
        resp = requests.post(url, headers=header_dict, json=payload, timeout=20, verify=verify_ssl)
        status = resp.status_code
        if status == 200:
            data = resp.json()
            choices = data.get("choices", [])
            msg = choices[0]["message"]["content"] if choices else "(vazio)"
            usage = data.get("usage", {})
            print(f"  ✓ [{label}] modelo={modelo}  →  {msg}")
            if usage:
                print(f"    Tokens: {usage}")
            return True
        elif status != 401:
            # 401 = não autenticou (esperado se header errado), outro código é info útil
            print(f"  [{label}] modelo={modelo}  →  HTTP {status}: {resp.text[:200]}")
        return False
    except Exception as e:
        print(f"  [{label}] modelo={modelo}  →  Erro: {e}")
        return False


def main():
    separador("TESTE DA API DE IA GENERATIVA PETROBRAS")
    print(f"URL Base: {BASE_URL}")
    print(f"Chave primária: {PRIMARY_KEY[:8]}...{PRIMARY_KEY[-4:]}")
    print(f"Chave secundária: {SECONDARY_KEY[:8]}...{SECONDARY_KEY[-4:]}")

    # Todas as combinações de headers para testar
    header_combos = []
    for key_name, key_val in [("PRI", PRIMARY_KEY), ("SEC", SECONDARY_KEY)]:
        # 1. Ocp-Apim-Subscription-Key (padrão Azure APIM)
        header_combos.append((f"{key_name}+Ocp-Apim", {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": key_val,
        }))
        # 2. api-key (padrão Azure OpenAI)
        header_combos.append((f"{key_name}+api-key", {
            "Content-Type": "application/json",
            "api-key": key_val,
        }))
        # 3. Authorization: Bearer
        header_combos.append((f"{key_name}+Bearer", {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key_val}",
        }))
        # 4. x-api-key
        header_combos.append((f"{key_name}+x-api-key", {
            "Content-Type": "application/json",
            "x-api-key": key_val,
        }))
        # 5. Ocp-Apim + api-key juntos
        header_combos.append((f"{key_name}+Ocp+apikey", {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": key_val,
            "api-key": key_val,
        }))
        # 6. Ocp-Apim + Bearer juntos
        header_combos.append((f"{key_name}+Ocp+Bearer", {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": key_val,
            "Authorization": f"Bearer {key_val}",
        }))
        # 7. Query param: subscription-key
        header_combos.append((f"{key_name}+QueryParam", {
            "Content-Type": "application/json",
            "_query_key": key_val,  # marcador especial
        }))

    # 1. Descobrir modelos
    separador("TESTE 1: Descobrir modelos via /models")
    # Tentar com Ocp-Apim + api-key juntos (mais provável)
    for label, hdrs in header_combos:
        if "_query_key" in hdrs:
            continue
        url = BASE_URL + "/models"
        try:
            resp = requests.get(url, headers=hdrs, timeout=12, verify=False)
            if resp.status_code == 200:
                data = resp.json()
                modelos_desc = [m.get("id", m.get("model", "?")) for m in data.get("data", [])]
                print(f"  ✓ [{label}] Modelos: {modelos_desc}")
                break
        except Exception:
            pass

    # 2. Force-brute: todas as combinações header x modelo
    separador("TESTE 2: Força-bruta header × modelo (engines/)")
    print(f"  Testando {len(header_combos)} headers × {len(MODELOS_TENTAR)} modelos...\n")

    modelo_ok = None
    header_ok = None
    sucessos = []  # Lista de tuplas (header_label, modelo)

    for label, hdrs in header_combos:
        # Tratar query param
        if "_query_key" in hdrs:
            key_val = hdrs["_query_key"]
            for modelo in MODELOS_TENTAR:
                url = ENGINE_URL.replace("{model}", modelo) + f"?subscription-key={key_val}"
                payload = {"messages": MENSAGEM_TESTE, "max_tokens": 50, "temperature": 0.1}
                try:
                    resp = requests.post(url, headers={"Content-Type": "application/json"},
                                         json=payload, timeout=20, verify=False)
                    if resp.status_code == 200:
                        data = resp.json()
                        choices = data.get("choices", [])
                        msg = choices[0]["message"]["content"] if choices else "(vazio)"
                        print(f"  ✓ [{label}] modelo={modelo}  →  {msg}")
                        sucessos.append((label, modelo))
                        if modelo_ok is None:
                            modelo_ok = modelo
                            header_ok = label
                    elif resp.status_code != 401:
                        print(f"  [{label}] modelo={modelo}  →  HTTP {resp.status_code}: {resp.text[:200]}")
                except Exception:
                    pass
            continue

        for modelo in MODELOS_TENTAR:
            if testar_combinacao(hdrs, modelo, label):
                sucessos.append((label, modelo))
                if modelo_ok is None:
                    modelo_ok = modelo
                    header_ok = label

    # 3. Tentar /chat/completions (sem /engines/)
    if not modelo_ok:
        separador("TESTE 3: /chat/completions (model no body)")
        for label, hdrs in header_combos[:6]:  # Só primeiras combinações
            for modelo in MODELOS_TENTAR[:4]:
                url = BASE_URL + "/chat/completions"
                payload = {"model": modelo, "messages": MENSAGEM_TESTE, "max_tokens": 50}
                try:
                    resp = requests.post(url, headers=hdrs, json=payload, timeout=20, verify=False)
                    if resp.status_code == 200:
                        data = resp.json()
                        choices = data.get("choices", [])
                        msg = choices[0]["message"]["content"] if choices else "(vazio)"
                        print(f"  ✓ [{label}] modelo={modelo}  →  {msg}")
                        sucessos.append((label, modelo))
                        if modelo_ok is None:
                            modelo_ok = modelo
                            header_ok = label
                    elif resp.status_code != 401:
                        print(f"  [{label}] modelo={modelo}  →  HTTP {resp.status_code}: {resp.text[:200]}")
                except Exception:
                    pass

    # 4. Diagnóstico final: mostrar headers que o servidor aceita
    if not modelo_ok:
        separador("DIAGNÓSTICO: Verificando quais headers não dão 401")
        for label, hdrs in header_combos[:6]:
            url = ENGINE_URL.replace("{model}", "gpt-4o")
            try:
                resp = requests.post(url, headers=hdrs, json={"messages": MENSAGEM_TESTE},
                                     timeout=12, verify=False)
                print(f"  [{label}] → HTTP {resp.status_code}")
            except Exception as e:
                print(f"  [{label}] → Erro: {e}")

    # Resumo
    separador("RESUMO")
    if sucessos:
        modelos_ok = list(dict.fromkeys([modelo for _, modelo in sucessos]))
        headers_ok = list(dict.fromkeys([label for label, _ in sucessos]))
        print(f"  ✓ API FUNCIONANDO!")
        print(f"  Primeiro sucesso: modelo={modelo_ok} | header={header_ok}")
        print(f"  Modelos que responderam: {modelos_ok}")
        print(f"  Headers que funcionaram: {headers_ok}")
        print(f"  Pronta para usar no projeto.")
    else:
        print(f"  ✗ Não foi possível autenticar.")
        print(f"  A API é acessível (recebemos HTTP 401), o que indica:")
        print(f"    1. As chaves estão chegando mas não no formato esperado")
        print(f"    2. Pode ser necessário um token OAuth/JWT em vez de subscription key")
        print(f"    3. Verifique na documentação da API o header correto")
        print(f"    4. Possível necessidade de autenticação via Azure AD/Entra ID")


if __name__ == "__main__":
    # Suprimir warnings de SSL para testes
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()
