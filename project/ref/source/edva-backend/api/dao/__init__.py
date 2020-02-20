#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
数据库配置信息

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/5/24
"""
from pymongo import MongoClient

# MONGO_SERVER = '10.103.240.191'
MONGO_SERVER = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DATABASE = 'edva'

client = MongoClient(MONGO_SERVER, MONGO_PORT)
db = client[MONGO_DATABASE]
