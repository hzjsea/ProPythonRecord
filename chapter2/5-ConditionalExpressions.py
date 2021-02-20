#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: 5-ConditionalExpressions.py.py
@time: 2021/2/19 11:03 上午
"""


# def test_value(value):
#     if value < 100:
#         return 'the value is just right'
#     else:
#         return 'the value is too big'
#
#
# test_value(20)
#
#


# def test_value(value: int):
#     return 'the value' + ('is just right' if value < 100 else 'is too  big')


def test_value(value: int):
    return 'the value' + ( value < 100 and ' is just right' or 'is too big')

print(test_value(20))