# -*- coding:utf-8 -*-

"""
python练习
"""
import random

#随机种子，同一种子，随机结果是一致的


random.seed(30)
ri = random.randint(1,50)
print(ri)

#dict() 函数用于创建一个字典。
dt = dict()
print(dt)

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict.__len__())
dict['address'] = '上海浦东新区'
print(dict.__len__())
print(dict['address'])
