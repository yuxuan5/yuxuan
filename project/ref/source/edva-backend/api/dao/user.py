#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/5/29
"""
import random
from operator import itemgetter

from . import db


def get_batch_users(users):
    result = []
    query_users = {'uid': {'$in': users}}
    for doc in db.user_info.find(query_users):
        uid = doc.get('uid', '')
        doc['eq'] = sum(get_user_eq(uid))
        result.append(doc)
    return result


def get_user_eq(uid):
    result = []
    query_user = {'uid': uid}
    for doc in db.user_eqs.find(query_user):
        result.append(doc.get('eqs'))
    if not result:
        return result
    else:
        return result[0]


def get_user_by_type(user_type):
    result = []
    query_users = {'type': user_type}
    for doc in db.user_info.find(query_users):
        uid = doc.get('uid')
        doc['eq'] = get_user_eq(uid)
        result.append(doc)
    return result


def get_user_in_circle(user_type, coord, max_distance):
    result = []
    query = {
        # 'type': user_type,
        'loc': {
            '$geoWithin': {
                '$centerSphere': [[coord['lng'], coord['lat']], max_distance / 6371000]
            }
        }
    }
    for doc in db.user_info.find(query):
        uid = doc.get('uid', '')
        doc['eq'] = sum(get_user_eq(uid))
        result.append(doc)
    return result


def get_user_in_box(user_type, bounds):
    result = []
    query = {
        # 'type': user_type,
        'loc': {
            '$geoWithin': {
                '$box': [[bounds['_southWest']['lng'], bounds['_southWest']['lat']],
                         [bounds['_northEast']['lng'], bounds['_northEast']['lat']]]
            }
        }
    }
    for doc in db.user_info.find(query):
        uid = doc.get('uid', '')
        doc['eq'] = sum(get_user_eq(uid))
        result.append(doc)
    return result


def sort_user_by_eq(users):
    sorted_user = sorted(users, key=itemgetter('eq'))
    return sorted_user


def get_resident_heat():
    return {}


def get_business_heat():
    return {}


if __name__ == "__main__":
    eq = []
    dd = get_user_by_type('01')
    for d in dd:
        eq.append(sum(d.get('eq')))
    print(eq.sort())
