from openai import OpenAI
import os

# How to get your Databricks token: https://docs.databricks.com/en/dev-tools/auth/pat.html
DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')
if not DATABRICKS_TOKEN:
    raise RuntimeError("Defina a variável de ambiente DATABRICKS_TOKEN com seu token Databricks.")
# Alternatively in a Databricks notebook you can use this:
# DATABRICKS_TOKEN = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()

client = OpenAI(
    api_key=DATABRICKS_TOKEN,
    base_url="https://adb-671799829240675.15.azuredatabricks.net/serving-endpoints"
)

response = client.chat.completions.create(
    model="databricks-claude-opus-4-6",
    messages=[
        {
            "role": "user",
            "content": "What is an LLM agent?"
        }
    ],
    max_tokens=5000
)

print(response.choices[0].message.content)