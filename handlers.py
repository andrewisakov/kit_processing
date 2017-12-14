#!/usr/bin/python3
# import json
import datetime
# import tornado.log
from tornado import web
# import tornado.websocket
# from tornado.concurrent import run_on_executor
# import concurrent.futures
# from tornado import gen
# from tornado.queues import Queue
# from tornado.escape import json_encode
# from tornado.escape import json_decode
from settings import logger
# import tmtapi
# import settings
import database


class Main(web.RequestHandler):
    commands = {'pay': database.pay, 'check': database.check}
    reduction = {'command': str, 'txn_id': str, 'account': str, 'sum': float,
                 'txn_date': lambda x: datetime.datetime.strptime(x, '%Y%m%d%H%M%S')}
    async def get(self):
        logger.debug(self.request.arguments)
        params = {k: self.reduction[k](v[0].decode()) for k, v in self.request.arguments.items()}
        logger.debug(params)
        self.set_status(404, 'NOT FOUND')
        self.set_header('content_type', 'application/text')
        result = ''
        if params['command'] in self.commands.keys():
            result = await self.commands[params['command']](**params)
            result = b'<?xml version="1.0" encoding="UTF-8" ?>' + result
            self.set_status(200, 'OK')
        logger.debug(result)
        self.write(result)
        self.flush()
