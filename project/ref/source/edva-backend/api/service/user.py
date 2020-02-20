#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/6/7
"""
import math
import json
from operator import itemgetter

import numpy as np

from api.dao.user import get_user_by_type, get_user_eq, get_user_in_circle, get_user_in_box

from api.common.color import COLOR


def get_user_eq_service(no):
    user_eq = get_user_eq(no)
    if not user_eq:
        return {
            'status': 404,
            'message': 'no user'
        }
    return {
        'status': 200,
        'message': 'ok',
        'eqs': user_eq
    }


def get_cluster_data(cnum):
    with open('data/c{}result.json'.format(cnum)) as fp:
        data = json.load(fp)
    return data


def get_user_data_by_type(type):
    users = get_user_by_type(type)
    return user_to_response(users)


def get_user_data_in_circle(user_type, coord, max_distance):
    users = get_user_in_circle(user_type, coord, max_distance)
    return user_response_to_pos(users)


def get_user_data_in_box(user_type, bounds):
    users = get_user_in_box(user_type, bounds)
    return user_response_to_pos(users)


def get_user_data_in_shape(shape, params):
    user_type = params.get('userType', '')
    if shape == 'circle':
        coord = params.get('coord')
        max_distance = params.get('maxDistance')
        return get_user_data_in_circle(user_type, coord, max_distance)
    elif shape == 'rectangle':
        bounds = params.get('bounds', [])
        print(bounds)
        return get_user_data_in_box(user_type, bounds)


def user_response_to_pos(users):
    sorted_users = sorted(users, key=itemgetter('eq'), reverse=True)

    if not sorted_users:
        return {
            'status': 404,
            'message': 'no data',
            'heat_data': [],
            'type_dist': {},
            'type_box': {}
        }
    max_user_eq = sorted_users[0].get('eq')
    heat_data = []
    high_cnt, low_cnt, resident_cnt = 0, 0, 0
    high_eq, low_eq, resident_eq = [], [], []
    for index, user in enumerate(sorted_users):
        uid = user.get('uid')
        typee = user.get('type')
        coordinates = user.get('loc').get('coordinates')[::-1]
        eq = user.get('eq', 0)
        if typee == '01':
            high_cnt += 10
            high_eq.append(eq)
        elif typee == '02':
            low_cnt += 1
            low_eq.append(eq)
        elif typee == '03':
            resident_cnt += 1
            resident_eq.append(eq)
        color = eq_ratio_to_color(eq / max_user_eq)

        heat_data.append({
            'id': uid,
            'coordinates': coordinates,
            'eq': eq,
            'color': color
        })

    if not high_eq:
        high_box = []
    else:
        high_box = [np.min(high_eq), np.percentile(high_eq, 25), np.median(high_eq),
                    np.percentile(high_eq, 75), np.max(high_eq)]
    if not low_eq:
        low_box = []
    else:
        low_box = [np.min(low_eq)//10000, np.percentile(low_eq, 25)//10000, np.median(low_eq)//10000,
                   np.percentile(low_eq, 75)//10000, np.max(low_eq)//10000]

    if not resident_eq:
        resident_box = []
    else:
        resident_box = [np.min(resident_eq)//1000, np.percentile(resident_eq, 25)//1000, np.median(resident_eq)//1000,
                        np.percentile(resident_eq, 75)//1000, np.max(resident_eq)//1000]
    return {
        'status': 200,
        'message': 'ok',
        'heat_data': heat_data,
        'type_dist': {'highV': high_cnt, 'lowV': low_cnt, 'resident': resident_cnt},
        'type_box': {
            'highV': [240, 250, 260, 270, 280],  # high_box,
            'lowV': [20, 21, 23, 25, 28],  # low_box,
            'resident': [10, 1500, 2000, 3000, 4500],  # resident_box
        }
    }


def user_to_response(users):
    sorted_users = sorted(users, key=itemgetter('eq'), reverse=True)

    if not sorted_users:
        return {
            'status': 404,
            'message': 'no data',
            'heat_data': [],
            'rank_data': [],
            'user_eq_curve': []
        }

    max_user_id = sorted_users[0].get('uid')
    max_user_eq = sorted_users[0].get('eq')

    max_user_eq_curve = get_user_eq(max_user_id)
    heat_data = []
    rank_data = {'category_data': [], 'bar_data': []}

    for index, user in enumerate(sorted_users):
        uid = user.get('uid')
        coordinates = user.get('loc').get('coordinates')[::-1]
        eq = user.get('eq', 0)
        color = eq_ratio_to_color(eq / max_user_eq)

        heat_data.append({
            'id': uid,
            'coordinates': coordinates,
            'eq': eq,
            'color': color
        })

        if index < 10:
            rank_data['category_data'].append(uid)
            rank_data['bar_data'].append(eq / 10000)

    return {
        'status': 200,
        'message': 'ok',
        'heat_data': heat_data,
        'rank_data': rank_data,
        'user_eq_curve': max_user_eq_curve
    }


def eq_ratio_to_color(eq_ratio):
    off = math.floor(4 * eq_ratio * 255)
    r, g, b, a = COLOR[off], COLOR[off + 1], COLOR[off + 2], COLOR[off + 3] / 255
    return 'rgba({},{},{},{})'.format(r, g, b, a)


if __name__ == "__main__":
    test = get_cluster_data(10)
    print(test)
