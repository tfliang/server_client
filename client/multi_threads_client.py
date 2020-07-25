# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 下午2:29
# @Author  : tf.liang
# @Email   : liangtengfei09@mails.ucas.ac.cn
# @File    : multi_threads_client.py

import queue
import threading
import requests
from utils import logger


class MultiThreadsClient:
    url = 'http://127.0.0.1:9001/v1/test/sleep'
    async_url = 'http://127.0.0.1:9001/v1/test/async_sleep'

    @classmethod
    def test_sleep_url(cls, n, sleep=1):
        workers = []
        for i in range(n):
            workers.append(threading.Thread(target=cls.one_request, args=(i, cls.url, sleep)))
            workers[-1].start()
        for th in workers:
            th.join()

    @classmethod
    def test_async_sleep_url(cls, n, sleep=1):
        workers = []
        for i in range(n):
            workers.append(threading.Thread(target=cls.one_request, args=(i, cls.async_url, sleep)))
            workers[-1].start()
        for th in workers:
            th.join()

    @classmethod
    def one_request(cls, tid, url, sleep):
        rs = requests.get(url=url, params={'ts': sleep})
        logger.info('thread: {}, response: {}'.format(tid, rs.json()))


if __name__ == '__main__':
    import time
    tic = time.time()
    MultiThreadsClient.test_sleep_url(5, 1)
    logger.info('sleep url: {}'.format(time.time() - tic))
    tic = time.time()
    MultiThreadsClient.test_async_sleep_url(5, 1)
    logger.info('sleep url: {}'.format(time.time() - tic))
