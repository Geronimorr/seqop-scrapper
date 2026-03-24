import os
from databricks_loader import DatabricksWellLoader

POCO = "1-APS-57"
HOST = "adb-671799829240675.15.azuredatabricks.net"
PATH = "/sql/1.0/warehouses/1fd972f888afd086"
TOKEN = os.environ.get("DATABRICKS_TOKEN")

if not TOKEN:
    raise RuntimeError("DATABRICKS_TOKEN nao definido no ambiente.")

loader = DatabricksWellLoader(
    server_hostname=HOST,
    http_path=PATH,
    access_token=TOKEN,
)

df_ops = loader.get_tempos_operacoes(POCO)

# 1. Todas as colunas
print("=== COLUNAS ===")
for i, col in enumerate(df_ops.columns):
    print(f"  {i:3d}. {col} ({df_ops[col].dtype})")

# 2. Amostra de 5 linhas (todas as colunas)
print("\n=== AMOSTRA ===")
print(df_ops.head(5).to_string())

# 3. Valores unicos das colunas categoricas chave
for col in ["TX_OPERACAO", "TX_ETAPA", "TX_ATIVIDADE", "IN_TIPO_TEMPO", "NR_FASE"]:
    if col in df_ops.columns:
        print(f"\n=== {col} - top 30 valores ===")
        print(df_ops[col].value_counts().head(30).to_string())

# 4. Tem coluna de descricao longa?
for col in df_ops.columns:
    if "DESC" in col.upper() or "OBS" in col.upper() or "OBJETIVO" in col.upper():
        print(f"\n=== {col} - amostra ===")
        print(df_ops[col].dropna().head(10).to_string())
