#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: 11-Import.py
@time: 2021/2/20 10:53 上午
"""

#
# try:
#     from hashlib import md5
# except ImportError
#     from md5 import new as md5


from chapter2.xx import *

if __name__ == '__main__':
    print(func1())
    print(func2())

