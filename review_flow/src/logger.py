import logging
import os


class LogHandler(logging.StreamHandler):
    def __init__(self):
        logging.StreamHandler.__init__(self)
        fmt = "%(asctime)s %(filename)-18s %(levelname)-8s: %(message)s"
        fmt_date = "%Y-%m-%d %H:%M:%S"
        formatter = logging.Formatter(fmt, fmt_date)
        self.setFormatter(formatter)


def get_logger(filename: str) -> logging.Logger:
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    logger = logging.getLogger(filename)

    logger.setLevel(log_level)
    return logger

