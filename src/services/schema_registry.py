import requests
from src.avro.events.generate_tasks_event import GenerateTask
import json


def register_schema(subject, schema_str, registry_url="http://localhost:8081"):
    headers = {"Content-Type": "application/vnd.schemaregistry.v1+json"}
    payload = {"schema": schema_str}
    response = requests.post(
        f"{registry_url}/subjects/{subject}/versions", headers=headers, json=payload
    )
    return response.json()


avro_schema = json.dumps(GenerateTask.avro_schema_to_python())
register_schema("task.requests-value", avro_schema)
