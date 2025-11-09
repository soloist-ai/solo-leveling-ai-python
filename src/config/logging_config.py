import logging
import sys
from src.config.config_loader import config


def setup_logging():
    logging_config = config["logging"]
    log_level = logging_config["level"]
    log_format = logging_config["format"]

    if log_format == "json":
        formatter = logging.Formatter(
            '{"time":"%(asctime)s", "level":"%(levelname)s", "name":"%(name)s", "message":"%(message)s"}'
        )
    else:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, log_level.upper()))
    root_logger.handlers.clear()

    if logging_config["handlers"]["console"]["enabled"]:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)

    for logger_name, logger_level in logging_config["loggers"].items():
        logger = logging.getLogger(logger_name)
        logger.setLevel(getattr(logging, logger_level.upper()))
