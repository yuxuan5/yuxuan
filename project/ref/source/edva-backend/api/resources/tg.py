#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/5/25
"""
import json

from flask_restful import Resource
from flask_restful import reqparse

from api.service.tg import get_user_data_within_tg, get_tg_eq_service
from api.dao.tg import get_tg_within_circle, get_top_k_heat_data, get_tg_within_rectangle
from api.service.user import get_user_eq_service


class TgHeat(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('tgno', type=str)
        super(TgHeat, self).__init__()

    def get(self):
        args = self.parse.parse_args()
        tgno = args['tgno']
        return get_user_data_within_tg(tgno)


class TgEq(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('type', type=str)
        self.parse.add_argument('no', type=str)
        super(TgEq, self).__init__()

    def get(self):
        args = self.parse.parse_args()
        types = args['type']
        no = args['no']
        if types == 'tg':
            return get_tg_eq_service(no)
        elif types == 'user':
            return get_user_eq_service(no)


class TopTgHeat(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('topk', type=int)
        super(TopTgHeat, self).__init__()

    def get(self):
        args = self.parse.parse_args()
        topk = args['topk']
        data = get_top_k_heat_data(topk)
        return data


class TgInCircle(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('coord', type=str)
        self.parse.add_argument('maxDistance', type=float)
        super(TgInCircle, self).__init__()

    def get(self):
        args = self.parse.parse_args()
        coordinate = json.loads(args['coord'])
        max_distance = args['maxDistance']
        data = get_tg_within_circle(coordinate, max_distance)
        return data


class TgInBox(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('bounds', type=str)
        super(TgInBox, self).__init__()

    def get(self):
        args = self.parse.parse_args()
        bounds = json.loads(args['bounds'])
        data = get_tg_within_rectangle(bounds)
        return data


if __name__ == "__main__":
    pass
