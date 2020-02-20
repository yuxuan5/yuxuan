#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/5/23
"""
from flask_restful import Resource
from flask_restful import reqparse


class Hello(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('name', type=str)
        self.parse.add_argument('age', type=int)
        super(Hello, self).__init__()

    def get(self):
        args = self.parse.parse_args()
        name = args['name']
        age = args['age']
        data = {'name': name, 'age': age}
        return data

    def post(self):
        pass


if __name__ == "__main__":
    pass
