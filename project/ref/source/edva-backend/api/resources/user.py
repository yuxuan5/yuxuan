#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/5/29
"""
import json

from flask_restful import Resource
from flask_restful import reqparse

from api.service.user import get_user_data_by_type, get_user_data_in_circle, \
    get_user_data_in_box, get_user_data_in_shape, get_cluster_data


class UserByType(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('type', type=str)
        super(UserByType, self).__init__()

    def get(self):
        args = self.parse.parse_args()
        type = args['type']
        return get_user_data_by_type(type)


class UserInCircle(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('userType', type=str)
        self.parse.add_argument('coord', type=str)
        self.parse.add_argument('maxDistance', type=float)
        super(UserInCircle, self).__init__()

    def get(self):
        args = self.parse.parse_args()
        user_type = args['userType']
        coordinate = json.loads(args['coord'])
        max_distance = args['maxDistance']
        data = get_user_data_in_circle(user_type, coordinate, max_distance)
        return data


class UserInBox(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('userType', type=str)
        self.parse.add_argument('bounds', type=str)
        super(UserInBox, self).__init__()

    def get(self):
        args = self.parse.parse_args()
        user_type = args['userType']
        bounds = json.loads(args['bounds'])
        data = get_user_data_in_box(user_type, bounds)
        return data


class UserInShape(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('shape', type=str)
        self.parse.add_argument('queryParams', type=str)
        super(UserInShape, self).__init__()

    def get(self):
        args = self.parse.parse_args()
        shape = args['shape']
        query_params = json.loads(args['queryParams'])
        print(shape)
        data = get_user_data_in_shape(shape, query_params)
        return data


class Cluster(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('cnum', type=str)
        super(Cluster, self).__init__()

    def get(self):
        args = self.parse.parse_args()
        cnum = args['cnum']
        result = get_cluster_data(cnum)
        return result


if __name__ == "__main__":
    pass
