#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/6/7
"""
from operator import itemgetter

from api.dao.tg import get_tg, get_tg_eq
from api.dao.user import get_batch_users, get_user_eq

from api.service.user import user_to_response


def get_user_data_within_tg(tgno):
    tgs = get_tg(tgno)

    tgs_info = []
    users = []
    for tg in tgs:
        users.extend(tg.get('users', []))
        tgs_info.append({
            'tgno': tg.get('tgno'),
            'byq_name': tg.get('byq_name'),
            'eq': tg.get('eq'),
            'coordinates': tg['loc']['coordinates'][::-1]
        })

    users_info = get_batch_users(users)

    return data_to_response(tgs_info, users_info)


def data_to_response(tg_info, users_info):
    res = user_to_response(users_info)
    res['tg_info'] = tg_info
    return res


def get_tg_eq_service(tgno):
    tg_eq = get_tg_eq(tgno)
    if not tg_eq:
        return {
            'status': 404,
            'message': 'no tg'
        }
    return {
        'status': 200,
        'message': 'ok',
        'eqs': tg_eq[0]
    }


if __name__ == "__main__":
    pass
