#!/usr/bin/python3
import hashlib
# import json
# import tornado.log
from tornado.httpclient import AsyncHTTPClient, HTTPError
from tornado.escape import json_encode, json_decode
# import settings
from settings import TMTAPI
from settings import logger


async def signature(data):
    # генератор подписи
    logger.debug('http_tmapi.signature generator')
    return hashlib.md5((data + TMTAPI['sign']).encode()).hexdigest()


async def tmtapi_request(request, post_data, method='POST'):  # json запрос
    logger.debug(f'http_tmapi.tmtapi_request {post_data}')
    post_data = json_encode(post_data)
    host, port = TMTAPI['host'], TMTAPI['post']
    url = f'https://{host}:{port}/common_api/1.0/{request}'
    headers = {
        'Signature': await signature(post_data),
        'Content-Type': 'application/json',
    }
    try:
        response = await AsyncHTTPClient(headers=headers, method=method).fetch(url)
        response = response.body if isinstance(response.body, str) \
            else response.body.decode(errors='ignore')
        response = json_decode(response), response.code
        logger.debug(f'http_tmapi.tmtapi_request {code} {response}')
    except HTTPError as e:
        logger.debug(e)
        response = post_data, response.code
    return response
