# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 下午2:28
# @Author  : tf.liang
# @Email   : liangtengfei09@mails.ucas.ac.cn
# @File    : async_client.py
import asyncio
import aiohttp
from utils import logger


class AsyncClient:
    url = 'http://127.0.0.1:9001/v1/test/sleep'
    async_url = 'http://127.0.0.1:9001/v1/test/async_sleep'

    @classmethod
    async def test_sleep_url(cls, n, sleep=1):
        async with aiohttp.ClientSession() as session:
            task = []
            for i in range(n):
                task.append(cls.one_request(session, cls.url, {'ts': sleep}))
            rs = await asyncio.gather(*task)
            for item in rs:
                logger.info('response: {}'.format(item))


    @classmethod
    async def test_async_sleep_url(cls, n, sleep=1):
        async with aiohttp.ClientSession() as session:
            task = []
            for i in range(n):
                task.append(cls.one_request(session, cls.async_url, {'ts': sleep}))
            rs = await asyncio.gather(*task)
            for item in rs:
                logger.info('response: {}'.format(item))

    @classmethod
    async def one_request(cls, session: aiohttp.ClientSession, url, params):
        async with session.get(url=url, params=params) as res:
            rs = await res.read()
            return rs


if __name__ == '__main__':
    import time

    tic = time.time()
    asyncio.run(AsyncClient.test_sleep_url(5, 1))
    logger.info('sleep url: {}'.format(time.time() - tic))
    tic = time.time()
    asyncio.run(AsyncClient.test_async_sleep_url(5, 1))
    logger.info('async sleep url: {}'.format(time.time() - tic))
