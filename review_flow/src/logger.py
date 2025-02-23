import logging
import os


class LogHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__()
        fmt = "%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s"
        fmt_date = "%Y-%m-%d %H:%M:%S"
        formatter = logging.Formatter(fmt, fmt_date)
        self.setFormatter(formatter)


def get_logger(name: str) -> logging.Logger:
    log_level = os.getenv("LOG_LEVEL", "DEBUG")

    logger = logging.getLogger(name)

    # Prevent adding multiple handlers in case of re-import
    if not logger.hasHandlers():
        handler = LogHandler()
        logger.setLevel(log_level)
        logger.addHandler(handler)

    return logger
