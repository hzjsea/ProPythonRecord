#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: 7-sequence unpacking.py
@time: 2021/2/19 6:10 下午
"""

url = "example.com"
prefix, suffix = url.split(".")
print(prefix, suffix)


def return_data():
    return 'hzj', 12


name, age = return_data()


def return_datas():
    return 'hzj', 12, 23, 45, 56


name, *ages = return_datas()
print(name, type(ages))  # hzj <class 'list'>



