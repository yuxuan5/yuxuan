#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/5/24
"""


class Path(dict):
    type = ''
    coordinates = []


class TGState(dict):
    tgno = ''
    path = Path()
    count = 0.0

if __name__ == "__main__":
    pass
