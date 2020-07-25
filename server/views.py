# -*- coding: utf-8 -*-
# @Time    : 2019-12-19 16:14
# @Author  : tf.liang
# @Email   : liangtengfei09@mails.ucas.ac.cn
# @File    : views.py


from server.test_delay_views import router as test_delay_router

__all__ = ['routers']


routers = [
    ('/test', test_delay_router),
]
