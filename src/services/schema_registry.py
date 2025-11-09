from src.services.schema_registry_service import schema_registry_service
from src.avro.events.generate_tasks_event import GenerateTask
from src.avro.events.save_tasks_event import SaveTask
import logging

logger = logging.getLogger(__name__)


def register_all_schemas():
    generate_schema = GenerateTask.avro_schema_to_python()
    schema_id_request = schema_registry_service.register_schema(
        "task.requests-value", generate_schema
    )
    if schema_id_request:
        logger.info(f"Registered GenerateTask schema with ID: {schema_id_request}")

    save_schema = SaveTask.avro_schema_to_python()
    schema_id_response = schema_registry_service.register_schema(
        "task.responses-value", save_schema
    )
    if schema_id_response:
        logger.info(f"Registered SaveTask schema with ID: {schema_id_response}")

    return {
        "request_schema_id": schema_id_request,
        "response_schema_id": schema_id_response,
    }


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.info("Registering schemas...")
    result = register_all_schemas()
    logger.info(f"Registration complete: {result}")
