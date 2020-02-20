#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/5/24
"""
from bson.json_util import dumps
from pymongo import MongoClient

MONGO_SERVER = '10.103.240.191'
MONGO_PORT = 27017
MONGO_DATABASE = 'edva'

client = MongoClient(MONGO_SERVER, MONGO_PORT)
db = client[MONGO_DATABASE]


def get_all_tg_heat_data():
    result = []
    for doc in db.tgstate.find():
        result.append(doc)
    return dumps(result)


def get_top_k_heat_data(k):
    query = [{'$sort': {'count': -1}}, {'$limit': k}]
    result = []
    for doc in db.tgstate.aggregate(query):
        result.append(doc)
    return dumps(result)


def get_tg_within_circle(coord, max_distance):
    query = {
        'path': {
            '$near': {
                '$geometry': {
                    'type': "Point",
                    'coordinates': [coord['lng'], coord['lat']]
                },
                '$maxDistance': max_distance
            }
        }
    }
    result = []
    for doc in db.tgstate.find(query):
        result.append(doc)
    return dumps(result)


if __name__ == "__main__":
    # get_tg_within_circle([121.5801795599, 31.079154649], 500)
    print(get_top_k_heat_data(20))
