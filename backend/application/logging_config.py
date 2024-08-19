import logging
from logging.config import dictConfig

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",
        },
        "detailed": {
            "format": "%(asctime)s - %(levelname)s - %(module)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "uvicorn": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

def setup_logging():
    dictConfig(LOGGING_CONFIG)
