"""
Script para acessar dados do RTO via API do SAURON.
Faz login, obtém token e consulta os endpoints do RTO.
"""

import requests
import json
import urllib3

# Desabilitar warnings de SSL (rede interna)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://sauron.petrobras.com.br/api"


def login(user: str, password: str) -> dict:
    """Autentica no SAURON e retorna os dados do login (incluindo token)."""
    resp = requests.post(
        f"{BASE_URL}/login",
        json={"user": user, "password": password},
        verify=False,
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()
    token = data.get("token")
    login_data = data.get("loginData", {})
    print(f"Login OK — usuário: {login_data.get('name', user)}")
    return data


def get_rto_48h(token: str) -> list:
    """Busca dados RTO das últimas 48h de todas as sondas."""
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(
        f"{BASE_URL}/octopus/48hrs/all",
        headers=headers,
        verify=False,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def get_tempos_operacionais(token: str, well: str) -> list:
    """Busca tempos operacionais (OpenWells) de um poço."""
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(
        f"{BASE_URL}/aida/temposOperacionais/{well}",
        headers=headers,
        verify=False,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def main():
    print("=== SAURON — Acesso ao RTO ===\n")

    user = input("Chave: ").strip()
    password = input("Senha: ").strip()

    # 1) Login
    try:
        login_resp = login(user, password)
    except requests.HTTPError as e:
        print(f"Erro no login: {e}")
        return
    except requests.ConnectionError:
        print("Erro de conexão. Verifique se está na rede Petrobras/VPN.")
        return

    token = login_resp["token"]

    # 2) Dados RTO 48h
    print("\nBuscando dados RTO (últimas 48h)...")
    try:
        rto_data = get_rto_48h(token)
    except requests.HTTPError as e:
        print(f"Erro ao buscar RTO: {e}")
        return

    # Agrupar por sonda
    sondas = {}
    for item in rto_data:
        if item and item.get("rig"):
            rig = item["rig"].strip().upper()
            if rig not in sondas:
                sondas[rig] = {"well": item.get("well", "").strip(), "registros": 0}
            sondas[rig]["registros"] += 1

    print(f"\nTotal de registros: {len(rto_data)}")
    print(f"Sondas encontradas: {len(sondas)}\n")

    for rig, info in sorted(sondas.items()):
        print(f"  {rig:<20} | Poço: {info['well']:<20} | {info['registros']} pontos")

    # 3) Salvar dados brutos
    with open("rto_dados_48h.json", "w", encoding="utf-8") as f:
        json.dump(rto_data, f, ensure_ascii=False, indent=2)
    print(f"\nDados salvos em rto_dados_48h.json")

    # 4) Buscar tempos operacionais de cada poço
    wells = list({info["well"] for info in sondas.values() if info["well"]})
    if wells:
        print(f"\nBuscando tempos operacionais de {len(wells)} poço(s)...")
        ow_data = {}
        for well in sorted(wells):
            try:
                ow = get_tempos_operacionais(token, well)
                ow_data[well] = ow
                print(f"  {well}: {len(ow)} atividades")
            except requests.HTTPError:
                print(f"  {well}: sem dados OW")

        with open("rto_tempos_operacionais.json", "w", encoding="utf-8") as f:
            json.dump(ow_data, f, ensure_ascii=False, indent=2)
        print(f"Tempos operacionais salvos em rto_tempos_operacionais.json")

    print("\nConcluído!")


if __name__ == "__main__":
    main()
