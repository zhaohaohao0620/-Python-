from logging import  INFO, Formatter, getLogger
from  logging.handlers import RotatingFileHandler


def log(module, log_file):
    M = 5
    MtoB = 1024 * 1024
    log_size = M * MtoB
    logger = getLogger(module)
    logger.setLevel(INFO)
    handle = RotatingFileHandler(log_file, maxBytes=log_size)
    formatter = Formatter('%(asctime)s - %(message)s')
    handle.setFormatter(formatter)
    logger.addHandler(handle)

    return logger

# https://cnblogs.com/nancyzhu/p/8551506.html
