#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
生成图表（chart）http://www.pygal.org
图标库安装：pip install pygal
转png安装：pip install CairoSVG
pip install lxml
pip install tinycss
pip install cssselect
sudo apt install python3-lxml
sudo apt install python3-dev
sudo apt install libffi-dev
sudo apt install libcairo2
"""

import pygal
# import cairosvg

bookname = ['树林里的小松鼠罗宾', '38-小狗花花的生日礼物', '371-卡卡搬新家', '376-灰姑娘', '2136-我爸爸', '424-鼹鼠的故事-鼹鼠和伙伴们', '299-区寄杀贼', '380-爱丽丝又不见了', '384-鹤妻', '300-诸葛恪得驴', '399-鼹鼠的故事-鼹鼠是个小画家', '298-幻想花园', '427-鼹鼠的故事-鼹鼠和电视', '185-舒科特和秘密魔法', '381-画家与颜色', '373-乐婆婆和她的小狗', '4974-100万只猫', '309-五个小英雄', '425-鼹鼠的故事-鼹鼠和宇宙飞船', '307-我才三岁嘛！', '4965-当我们在一起时', '377-童话里的爱丽丝', '4968-是谁更奇怪呢', '305-斗年兽', '378-菲尼精与森林大火', '3704-我想有个弟弟', '304-李寄除妖', '4972-影子', '5173-Guess How Much I Love You', '2160-鲸鱼', '5170-Yo!Yes', '388-丁香树', '5690-The Tiny Seed', '3322-叮咚与闪亮 闪亮想妈妈', '387-咔嗒', '311-你是我的奇迹', '5166-Pancakes,Pancakes', '4967-宝贝，不可以', '5168-Hushabye Lily', '5164-Swimmy', '4971-皮特猫3_我拯救了圣诞节', '4778-彩虹花', '4973-小羊睡不着', '5171-My Mum', "5165-It's Mine", '3302-叮咚与闪亮 草原大营救', '5172-No,David!', '5169-Goldilocks and The Three Bears', '3310-叮咚与闪亮_飞向蓝天', '3319-叮咚和闪亮-可爱的朋友们', '3320-叮咚与闪亮 一颗神秘的蛋', '4975-熊爸爸不怕']
score = [0.0, 0.562, 0.595, 0.635, 0.705, 0.714, 0.718, 0.726, 0.732, 0.747, 0.757, 0.804, 0.806, 0.812, 0.812, 0.813, 0.824, 0.84, 0.857, 0.873, 0.883, 0.888, 0.89, 0.905, 0.908, 0.91, 0.917, 0.926, 0.928, 0.937, 0.944, 0.946, 0.953, 0.955, 0.96, 0.967, 0.967, 0.97, 0.971, 0.975, 0.976, 0.978, 0.983, 0.987, 0.994, 0.995, 0.995, 0.996, 1.0, 1.0, 1.0, 1.0]
recall = [0.0, 0.0, 0.118, 0.0, 0.167, 0.333, 0.318, 0.333, 0.5, 0.615, 0.222, 0.364, 0.0, 0.0, 0.0, 0.474, 0.231, 0.176, 0.333, 0.706, 0.0, 0.783, 0.55, 0.571, 0.643, 0.037, 0.8, 0.353, 1.0, 0.667, 1.0, 0.4, 0.826, 0.778, 0.905, 0.84, 0.679, 0.909, 1.0, 0.95, 0.812, 0.8, 0.893, 1.0, 1.0, 0.95, 0.952, 1.0, 1.0, 1.0, 1.0, 1.0]
accuracy = [0.0, 0.0, 0.222, 0.0, 0.529, 0.385, 0.579, 0.125, 0.2, 0.471, 0.4, 0.545, 0.0, 0.0, 0.0, 0.625, 0.437, 0.429, 0.308, 0.75, 0.0, 0.81, 0.958, 0.5, 0.474, 0.333, 0.556, 0.462, 0.542, 0.81, 0.444, 0.667, 0.682, 0.833, 0.632, 0.818, 0.529, 0.833, 0.72, 0.72, 0.929, 0.833, 0.806, 0.739, 0.875, 1.0, 0.909, 0.905, 1.0, 1.0, 1.0, 1.0]

hist = pygal.HorizontalBar(y_label_rotation=-20, legend_at_bottom=True)
hist.title = "绘本识别结果"
hist.x_labels = map(str, bookname)
hist.add('得分', score)
hist.add('召回', recall)
hist.add('精准', accuracy)
hist.render()
hist.render_to_file("test.svg")
# hist.render_in_browser()
# hist.render_to_png("test.png")

# import pygal
#
# bar_chart = pygal.Bar()
# bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13])
# # bar_chart.render_to_file('bar_cart.svg')
# bar_chart.render_in_browser()




