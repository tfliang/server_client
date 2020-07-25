# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 下午12:20
# @Author  : tf.liang
# @Email   : liangtengfei09@mails.ucas.ac.cn
# @File    : utils.py
import os
import logging


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_PATH = os.path.join(BASE_DIR, 'logs')
LOG_LEVEL = logging.DEBUG
LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s - %(filename)s - %(module)s - %(funcName)s - %(process)d - %(thread)d - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s - %(filename)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'web_file': {
            'level': 'DEBUG',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 3,
            'filename': os.path.join(LOG_PATH, 'web.log'),
            'formatter': 'standard'
        },
        'main_file': {
            'level': 'DEBUG',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 3,
            'formatter': 'standard',
            'filename': os.path.join(LOG_PATH, 'main.log'),
        },
    },

    'loggers': {
        'web': {
            'handlers': ['console', 'web_file'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
        'main': {
            'handlers': ['console', 'main_file'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
    },
}


from logging.config import dictConfig
logging.config.dictConfig(LOG_CONFIG)

logger = logging.getLogger('main')