#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/8/9
"""
import json
from operator import itemgetter
from api.service.user import get_user_by_type


if __name__ == "__main__":
    eq = []
    result = get_user_by_type('01')
    for doc in result:
        eq.append({
            'uid': doc.get('uid'),
            'loc': doc.get('loc').get('coordinates'),
            'eq': sum(doc.get('eq'))
        })
    sorted_eq = sorted(eq, key=itemgetter('eq'), reverse=True)
    with open('highV.json', 'w') as f:
        json.dump(sorted_eq, f, indent=4)
