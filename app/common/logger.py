# -*- coding: utf-8 -*-
import logging
from os import getenv


def getLogger(name: str) -> logging.Logger:
    log_name = getenv("LOG_NAME", name)
    if not (log_name == name):
        log_name += ":${name}"
    return logging.getLogger(log_name)
