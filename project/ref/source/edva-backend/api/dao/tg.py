#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/5/29
"""
from bson.json_util import dumps

from . import db


def get_all_tg_heat_data():
    result = []
    for doc in db.tg_info.find():
        result.append(doc)
    return dumps(result)


def get_tg(tgno):
    result = []
    query_tg = {'tgno': tgno}
    for doc in db.tg_info.find(query_tg):
        result.append(doc)
    return result


def get_batch_tg(tgs):
    result = []
    query_tgs = {'tgno': {'$in': tgs}}
    for doc in db.tg_info.find(query_tgs):
        result.append(doc)
    return result


def get_tg_eq(tgno):
    result = []
    query_tg_eq = {'tgno': tgno}
    for doc in db.tg_eqs.find(query_tg_eq):
        result.append(doc.get('eqs'))
    return result


def get_top_k_heat_data(k):
    query = [{'$sort': {'count': -1}}, {'$limit': k}]
    result = []
    for doc in db.tg_info.aggregate(query):
        result.append(doc)
    return dumps(result)


def get_tg_within_circle(coord, max_distance):
    query = {
        'path': {
            '$geoWithin': {
                '$centerSphere': [[coord['lng'], coord['lat']], max_distance/6371000]
            }
        }
    }
    result = []
    for doc in db.tg_info.find(query):
        result.append(doc)
    return dumps(result)


def get_tg_within_rectangle(bounds):
    print(type(bounds), bounds)
    # specify the bottom-left and top-right corners of box
    query = {
        'path': {
            '$geoWithin': {
                '$box': [[bounds['_southWest']['lng'], bounds['_southWest']['lat']],
                         [bounds['_northEast']['lng'], bounds['_northEast']['lat']]]
            }
        }
    }
    result = []
    for doc in db.tg_info.find(query):
        result.append(doc)
    return dumps(result)


if __name__ == "__main__":
    get_tg_within_circle([121.5801795599, 31.079154649], 500)
    # print(get_top_k_heat_data(20))
