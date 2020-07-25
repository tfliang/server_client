# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 下午12:18
# @Author  : tf.liang
# @Email   : liangtengfei09@mails.ucas.ac.cn
# @File    : test_delay_views.py
from fastapi import APIRouter
import time
import asyncio


router = APIRouter()


@router.get('/sleep')
async def sleep(ts: int):
    time.sleep(ts)
    return {'sleep': ts}


@router.get('/async_sleep')
async def async_sleep(ts: int):
    await asyncio.sleep(ts)
    return {'async sleep': ts}




