#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: 9-Generator  Expressions.py
@time: 2021/2/20 10:11 上午
"""


gen = (value for value in range(10, 30) if value > 20)
print(type(gen)) # <class 'generator'>


dict = {value: str(value) for value in range(10) if value > 5}
print(dict)  # {6: '6', 7: '7', 8: '8', 9: '9'}


import itertools

print(list(itertools.chain(range(3), range(4)))) # [0, 1, 2, 0, 1, 2, 3]


print(list(zip(range(3), reversed(range(10)))))  # [(0, 9), (1, 8), (2, 7)]



