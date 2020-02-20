#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/6/7
"""
from operator import itemgetter

from api.dao.line import get_line, get_all_lines
from api.dao.tg import get_batch_tg, get_tg_eq


def get_all_line_name():
    all_line_name = []
    lines = get_all_lines()
    for line in lines:
        all_line_name.append(line.get('lname'))
    return all_line_name


def get_tg_data_within_line(lid):
    lines = get_line(lid)

    tgs = []
    for line in lines:
        tgs.extend(line.get('tgs', []))

    tgs_info = get_batch_tg(tgs)

    heat_data = []
    rank_data = {'category_data': [], 'bar_data': [], 'tgno': []}

    sorted_tg = sorted(tgs_info, key=itemgetter('eq'))
    max_tg = sorted_tg[-1].get('tgno')
    tg_eq_curve = get_tg_eq(max_tg)

    for index, tg in enumerate(sorted_tg[::-1]):
        coord_and_eq = tg.get('loc').get('coordinates')[::-1]
        coord_and_eq.append(tg.get('eq', 0))
        heat_data.append(coord_and_eq)

        if index < 10:
            rank_data['category_data'].append(tg.get('byq_name'))
            rank_data['bar_data'].append(tg.get('eq') / 10000)
            rank_data['tgno'].append(tg.get('tgno'))

    return {
        'code': 200,
        'message': 'ok',
        'heat_data': heat_data,
        'rank_data': rank_data,
        'tg_eq_curve': tg_eq_curve
    }


if __name__ == "__main__":
    pass
