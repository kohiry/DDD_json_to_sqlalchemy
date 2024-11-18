import logging

from src.core import settings

__all__ = ["get_logger"]


def get_logger(name=__name__):
    """
    Create and return logger with package name.
    By default, using __name__.
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, settings.LOG_LEVEL, logging.INFO))

    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(getattr(logging, settings.LOG_LEVEL, logging.DEBUG))

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        ch.setFormatter(formatter)

        logger.addHandler(ch)

    return logger
