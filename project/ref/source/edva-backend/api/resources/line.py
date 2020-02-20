#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/5/29
"""
from flask_restful import Resource
from flask_restful import reqparse

from api.service.line import get_all_line_name, get_tg_data_within_line


class Line(Resource):
    def get(self):
        return get_all_line_name()


class LineHeat(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('lid', type=str)
        super(LineHeat, self).__init__()

    def get(self):
        args = self.parse.parse_args()
        lid = args['lid']
        return get_tg_data_within_line(lid)


if __name__ == "__main__":
    pass
