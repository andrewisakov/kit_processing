#!/usr/bin/python3
import os
import logger as logger_


APP_DIR = os.path.dirname(__file__)
SQL_DIR = os.path.join(APP_DIR, 'sql')
logger = logger_.rotating_log(os.path.join(APP_DIR, 'kit_processing.log'), 'kit_processing_log')

PORT = 8443
settings = {
    'cookie_secret': '61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=',
    'login_url': '/login',
    'xsrf_cookies': True,
    'debug': True,
    'autoreload': True,
    'compiled_template_cache': False,
    'serve_traceback': True,
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'archive_path': os.path.join(os.path.dirname(__file__), 'static'),
    'log_file_max_size': str(10*1024*1024),
    'log_file_prefix': 'kit_processing.log',
    # 'ssl_options': {
    #     "certfile": os.path.join("certs/myserver.crt"),
    #     "keyfile": os.path.join("certs/myserver.key"),
    # },
}

OK = 0  # не фатал
RETRY_LATER = 1  # не фатал
BAD_ACCOUNT = 4
MISTAKE_ACCOUNT = 5
PAYMENT_NOT_COMPLETE = 90  # не фатал
SOME_ERROR = 300


TMTAPI = {'host': '127.0.0.1', 'port': 8089, 'sign': '1292'}
DSN = 'user=sysdba password=admin database=C:\\tme_db.fdb host=127.0.0.1 charset=win1251'
FDB = {'user': 'sysdba', 'password': 'admin',
       'database': 'd:\\tme_db.fdb', 'host': '127.0.0.1',
       'charset': 'win1251'}
