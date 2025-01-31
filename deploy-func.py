import os
import shutil
import tempfile
from cognite.client import CogniteClient, ClientConfig, global_config
from cognite.client.credentials import OAuthClientCredentials

# Charger les secrets depuis les variables d'environnement
os.environ['MAMATASECRET'] = os.getenv('MAMATASECRET')
tenant_id = os.getenv('TENANT_ID')
client_id = os.getenv('CLIENT_ID')
client_secret = os.environ['MAMATASECRET']

cluster = "westeurope-1"
base_url = f"https://{cluster}.cognitedata.com"
creds = OAuthClientCredentials(
    token_url=f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token",
    client_id=client_id,
    client_secret=client_secret,
    scopes=[f"{base_url}/.default"],
    audience=base_url
)

cnf = ClientConfig(
    client_name="pythonSDK",
    base_url=base_url,
    project="mamata-dev",
    credentials=creds
)

global_config.default_client_config = cnf
client = CogniteClient()

folder = tempfile.mkdtemp()
shutil.copy("./handler.py", f"{folder}/handler.py")

requirements = """pandas
numpy
pytz
scipy
cognite-logger
python-dateutil
pydantic"""
with open(f"{folder}/requirements.txt", "w") as req:
    req.write(requirements)

zip_name = folder
shutil.make_archive(zip_name, 'zip', folder)

file_external_id = "CI-test-function-function"
cdf_file = client.files.upload(external_id=file_external_id, path=f"{zip_name}.zip", overwrite=True)

function_external_id = "CI-test-function"
function_description = "This is a test function to deploy with github actions."
author = "younes.essoualhi@mamata.eu"

try:
    client.functions.delete(external_id=function_external_id)
except:
    print("Function does not exist")
finally:
    func = client.functions.create(
        name=function_external_id,
        description=function_description,
        owner=author,
        external_id=function_external_id,
        file_id=cdf_file.id,
        runtime="py311"
    )
    schedule = client.functions.schedules.create(
        name="Every 1 minutes - calculate KPIs",
        cron_expression="*/1 * * * *",
        function_id=func.id,
        data={"key": "value"},
        client_credentials={"client_id": client_id, "client_secret": client_secret}
    )

shutil.rmtree(folder)