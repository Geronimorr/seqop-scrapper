import os
import pandas as pd
from databricks_loader import DatabricksWellLoader

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

conn = loader._connect()
cur = conn.cursor()
cur.execute("""
SELECT
    table_catalog,
    table_schema,
    table_name,
    column_name,
    ordinal_position,
    data_type
FROM dt0013_prd.information_schema.columns
WHERE table_schema = 'registros_operacionais'
ORDER BY table_name, ordinal_position
""")
rows = cur.fetchall()
cur.close()
conn.close()

cols = [
    "table_catalog", "table_schema", "table_name",
    "column_name", "ordinal_position", "data_type"
]
df = pd.DataFrame(rows, columns=cols)

csv_all = "colunas_registros_operacionais.csv"
csv_resumo = "resumo_colunas_por_tabela.csv"

df.to_csv(csv_all, index=False, encoding="utf-8")
resumo = df.groupby("table_name", as_index=False).agg(total_colunas=("column_name", "count"))
resumo = resumo.sort_values(["total_colunas", "table_name"], ascending=[False, True])
resumo.to_csv(csv_resumo, index=False, encoding="utf-8")

print(f"Total de tabelas: {resumo.shape[0]}")
print(f"Total de colunas no schema: {df.shape[0]}")
print(f"Arquivos gerados: {csv_all} | {csv_resumo}")
print("\nTop 20 tabelas com mais colunas:")
print(resumo.head(20).to_string(index=False))
