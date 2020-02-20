#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/5/22
"""
from flask import Flask

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__, instance_relative_config=True)

# 日志配置
handler = RotatingFileHandler('api.log', maxBytes=10000, backupCount=1)
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s: %(lineno)d]'))
handler.setLevel(logging.INFO)

app.logger.addHandler(handler)


from .api import *
