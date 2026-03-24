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

conn = loader._connect()
cursor = conn.cursor()
cursor.execute("""
    SELECT table_name 
    FROM dt0013_prd.information_schema.tables 
    WHERE table_schema = 'registros_operacionais'
    ORDER BY table_name
""")
for row in cursor.fetchall():
    print(row[0])
cursor.close()
conn.close()
