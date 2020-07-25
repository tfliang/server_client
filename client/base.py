# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 下午2:29
# @Author  : tf.liang
# @Email   : liangtengfei09@mails.ucas.ac.cn
# @File    : base.py
import requests
from utils import logger


class BaseClient:
    url = 'http://127.0.0.1:9001/v1/test/sleep'
    async_url = 'http://127.0.0.1:9001/v1/test/async_sleep'

    @classmethod
    def test_sleep_url(cls, n, sleep=1):
        for i in range(n):
            rs = requests.get(url=cls.url, params={'ts': sleep})
            logger.info(rs.json())

    @classmethod
    def test_async_sleep_url(cls, n, sleep=1):
        for i in range(n):
            rs = requests.get(url=cls.url, params={'ts': sleep})
            logger.info(rs.json())



if __name__ == '__main__':
    import time
    tic = time.time()
    BaseClient.test_sleep_url(5)
    logger.info('sleep url: {}'.format(time.time() - tic))
    tic = time.time()
    BaseClient.test_async_sleep_url(5)
    logger.info('async sleep url: {}'.format(time.time() - tic))


