#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/5/29
"""
from api.dao.tg import get_tg_within_circle

if __name__ == "__main__":
    coord = {
        'lat': 31.1117,
        'lng': 121.6900
    }
    print(get_tg_within_circle(coord, 500))
