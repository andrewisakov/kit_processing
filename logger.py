#!/usr/bin/python3
import logging
from logging.handlers import TimedRotatingFileHandler


def rotating_log(path, name, log_level=logging.DEBUG):
    # global logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # add a rotating handler
    formatter = logging.Formatter('%(asctime)s %(module)s [%(lineno)s] %(levelname)s %(message)s')

    handler = TimedRotatingFileHandler(path, when='midnight', backupCount=5)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
