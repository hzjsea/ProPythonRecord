#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: List  Comprehensions.py.py
@time: 2021/2/19 6:26 下午
"""

output = []

for value in range(10, 100):
    if value < 20:
        output.append(str(value))


output = [str(value) for value in range(10, 100) if value < 20]


print(min([value for value in range(1, 100) if value < 20]))