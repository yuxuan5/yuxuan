#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/8/5
"""
import os
import json

import pandas as pd
from sklearn.cluster import KMeans


def get_cluster_result(n_cluster):
    result_path = 'data/c{}result.json'.format(n_cluster)
    if os.path.exists(result_path):
        with open(result_path) as fp:
            data = json.load(fp)
    else:
        data = clustering(n_cluster)

    return data


def clustering(n_cluster):
    feats = pd.read_csv('data/feats.csv', index_col=0).dropna(axis=0, how='any')
    vis_feats = pd.read_csv('data/vis_feats.csv', index_col=0)
    X = feats.as_matrix()
    kmeans = KMeans(n_clusters=n_cluster).fit(X)
    feats['label'] = kmeans.labels_
    joined_feats = feats[['sum', 'label']].join(vis_feats, how='left', lsuffix='feats', rsuffix='vis')
    return concat_and_save_result(joined_feats, n_cluster)


def concat_and_save_result(joined_feats, n_cluster):
    result = []
    for i in range(n_cluster):
        cluster_i = joined_feats[joined_feats['label'] == i]
        class_dict = {'cid': n_cluster}
        # box-plot
        total_eq = cluster_i[['sum']]
        box_min = total_eq.min(axis=0).values[0]
        box_q1 = total_eq.quantile(q=0.25, axis=0).values[0]
        box_median = total_eq.median(axis=0).values[0]
        box_q3 = total_eq.quantile(q=0.75, axis=0).values[0]
        box_max = total_eq.max(axis=0).values[0]
        class_dict['box'] = [box_min, box_q1, box_median, box_q3, box_max]
        # series-pie
        series_list = []
        means = cluster_i.mean(axis=0)
        for j in range(12):
            total = means['{}-total'.format(j+1)]
            unused = means['{}-unused'.format(j+1)]
            eq1 = means['{}-eq1'.format(j+1)]
            eq2 = means['{}-eq2'.format(j+1)]
            eq3 = means['{}-eq3'.format(j+1)]
            eq4 = means['{}-eq4'.format(j+1)]
            series_month = {'total': total, 'unused': unused, 'eq1': eq1, 'eq2': eq2, 'eq3': eq3, 'eq4': eq4}
            series_list.append(series_month)
        class_dict['series'] = series_list
        # number of class
        class_dict['num'] = cluster_i.shape[0]
        result.append(class_dict)

    with open('data/c{}result.json'.format(n_cluster), 'w') as fp:
        json.dump(result, fp, indent=4)

    return result


def random_cluster():
    userClassWeight = [{
        # 空置房
        'box': [0.1, 0.2, 0.3, 0.4, 0.5],
        'cnt': 2.5,
        'all': 1, 'peak': 1, 'ave': 1, 'extreme': 1, 'valley': 1,
        'monthWeight': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'cyclical': [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    }, {
        # 正常低用电量用户
        'box': [1, 1.2, 1.3, 1.4, 1.5],
        'cnt': 2.5,
        'all': 3, 'peak': 1, 'ave': 1, 'extreme': 1, 'valley': 3,
        'monthWeight': [3, 2, 1, 1, 1, 2, 2.5, 3, 1, 1, 2, 2.5],
        'cyclical': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    }, {
        # 正常高用电量用户
        'box': [2, 2.5, 3, 3.5, 4],
        'cnt': 2,
        'all': 5, 'peak': 1, 'ave': 1, 'extreme': 1, 'valley': 3,
        'monthWeight': [3, 2, 1, 1, 1, 2, 2.5, 3, 1, 1, 2, 2.5],
        'cyclical': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    }, {
        # 春节回家
        'box': [1, 1.2, 1.3, 1.4, 1.5],
        'cnt': 0.5,
        'all': 3, 'peak': 1, 'ave': 1, 'extreme': 1, 'valley': 3,
        'monthWeight': [3, 2, 1, 1, 1, 2, 2.5, 3, 1, 1, 2, 2.5],
        'cyclical': [1, 0.3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    }, {
        # 全年无波动，且用电量大
        'box': [3, 3.5, 4, 4.5, 5],
        'cnt': 1.5,
        'all': 5, 'peak': 5, 'ave': 3, 'extreme': 5, 'valley': 3,
        'monthWeight': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        'cyclical': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    }, {
        # 全年无波动，用电量小
        'box': [0.1, 0.2, 0.3, 0.4, 0.5],
        'cnt': 1,
        'all': 2, 'peak': 5, 'ave': 3, 'extreme': 5, 'valley': 1,
        'monthWeight': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'cyclical': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    }]
    res = []
    for user_weight in userClassWeight:
        series = []
        for month in range(12):
            series.append({
                "total": user_weight['all']*user_weight['monthWeight'][month]*1000000,
                "unused": 30-user_weight['cyclical'][month]*30,
                "eq1": user_weight['peak']*user_weight['monthWeight'][month]*1000000,
                "eq2": user_weight['ave']*user_weight['monthWeight'][month]*1000000,
                "eq3": user_weight['extreme']*user_weight['monthWeight'][month]*1000000,
                "eq4": user_weight['valley']*user_weight['monthWeight'][month]*1000000
            })
        res.append({'uid': 6, 'box': user_weight['box'], 'series': series, 'num': user_weight['cnt']})

    with open('../../data/c6result.json', 'w') as f:
        json.dump(res, f, indent=4)


if __name__ == "__main__":
    # get_cluster_result(11)
    random_cluster()
