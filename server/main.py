# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 下午12:34
# @Author  : tf.liang
# @Email   : liangtengfei09@mails.ucas.ac.cn
# @File    : main.py

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from server.views import routers
from utils import logger


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

pre_url = '/v1'


for router_prefix, router in routers:
    app.include_router(
        router=router,
        prefix=pre_url + router_prefix
    )