from faststream.kafka import KafkaBroker
from src.config.config_loader import (
    get_kafka_bootstrap_servers,
    get_kafka_topics,
    get_kafka_consumer_config,
    get_kafka_producer_config,
)
import logging

logger = logging.getLogger(__name__)


def create_kafka_broker() -> KafkaBroker:
    """Создает Kafka broker с настройками из application.yml"""

    bootstrap_servers = get_kafka_bootstrap_servers()
    logger.info(f"Creating Kafka broker: {bootstrap_servers}")

    broker = KafkaBroker(bootstrap_servers)

    return broker


def get_topics() -> dict:
    return get_kafka_topics()


def get_consumer_config() -> dict:
    return get_kafka_consumer_config()


def get_producer_config() -> dict:
    return get_kafka_producer_config()


kafka_broker = create_kafka_broker()
topics = get_topics()
