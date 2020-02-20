#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/5/29
"""
from . import db


def get_all_lines():
    result = []
    for doc in db.line_info.findAll():
        result.append(doc)
    return result


def get_line(lid):
    result = []
    query_line = {'lid': lid}
    for doc in db.line_info.find(query_line):
        result.append(doc)
    return result


if __name__ == "__main__":
    get_line('270001815')
