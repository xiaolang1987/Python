#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
生成图表（chart）
pip install pygal
"""

import pygal

lists = [5, 2, 9, 19, 30]

hist = pygal.Bar()

hist.title = "图表演示"
hist.x_labels = ['a', 'b', 'c', 'd']
hist.x_title = "x轴"
hist.y_title = "y轴"

hist.add('绘本召回率', lists)
hist.render_to_file('test.svg')

