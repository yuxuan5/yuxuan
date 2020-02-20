#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/5/22
"""
from flask_restful import Api
from flask_restful.utils import cors
from . import app

from api.resources.test import Hello

from api.resources.line import Line, LineHeat
from api.resources.tg import TgHeat, TgEq, TopTgHeat, TgInCircle, TgInBox
from api.resources.user import UserByType, UserInCircle, UserInBox, UserInShape, Cluster

api = Api(app)
api.decorators = [cors.crossdomain(origin='*')]


api.add_resource(Hello, '/hello')

api.add_resource(Line, '/line/query')
api.add_resource(LineHeat, '/line/heat')

api.add_resource(TgHeat, '/tg/heat')
api.add_resource(TgEq, '/tg/eq')
api.add_resource(TopTgHeat, '/tg/topTg')
api.add_resource(TgInCircle, '/tg/incircle')
api.add_resource(TgInBox, '/tg/inbox')

api.add_resource(UserByType, '/user/bytype')
api.add_resource(UserInCircle, '/user/incircle')
api.add_resource(UserInBox, '/user/inbox')
api.add_resource(UserInShape, '/user/inshape')

api.add_resource(Cluster, '/cluster')
