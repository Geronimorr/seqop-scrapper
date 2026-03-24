import os
import pandas as pd
from databricks_loader import DatabricksWellLoader


token = os.environ.get("DATABRICKS_TOKEN")
if not token:
  raise RuntimeError("Defina DATABRICKS_TOKEN no ambiente antes de executar este script.")

loader = DatabricksWellLoader(
    server_hostname="adb-671799829240675.15.azuredatabricks.net",
    http_path="/sql/1.0/warehouses/1fd972f888afd086",
  access_token=token,
)

conn = loader._connect()

q1 = """
select NM_POCO, max(DT_INICIO_ATIVIDADE) as max_dt, count(*) as n
from dt0013_prd.registros_operacionais.tempos_operacoes_completa
where upper(NM_POCO) like '%8-MRO-35DA-RJS%'
group by NM_POCO
order by max_dt desc
"""

q2 = """
select NM_POCO, DT_INICIO_ATIVIDADE, TX_ATIVIDADE, TX_OPERACAO
from dt0013_prd.registros_operacionais.tempos_operacoes_completa
where upper(NM_POCO) like '%8-MRO-35DA-RJS%'
  and DT_INICIO_ATIVIDADE >= '2026-03-10'
order by DT_INICIO_ATIVIDADE desc
limit 80
"""

q3 = """
select NM_POCO, max(DT_INICIO_ATIVIDADE) as max_dt, count(*) as n
from dt0013_prd.registros_operacionais.tempos_operacoes_completa
where DT_INICIO_ATIVIDADE >= '2026-03-11'
  and (
    upper(NM_POCO) like '%8-MRO%'
    or upper(NM_POCO) like '%MRO-35%'
    or upper(NM_POCO) like '%35DA%'
  )
group by NM_POCO
order by max_dt desc
"""

df1 = pd.read_sql(q1, conn)
df2 = pd.read_sql(q2, conn)
df3 = pd.read_sql(q3, conn)
conn.close()

print("=== NM_POCO com 8-MRO-35DA-RJS ===")
print(df1.to_string(index=False))
print("\n=== Registros desde 2026-03-10 ===")
if df2.empty:
    print("(sem registros)")
else:
    print(df2[["NM_POCO", "DT_INICIO_ATIVIDADE"]].to_string(index=False))
print("\n=== Possiveis nomes similares com dados >= 2026-03-11 ===")
if df3.empty:
    print("(sem nomes similares)")
else:
    print(df3.to_string(index=False))
