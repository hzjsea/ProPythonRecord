#!/usr/bin/env python3
# encoding: utf-8
"""
@author: hzjsea
@file: 1-iteration.py
@time: 2021/2/19 9:21 上午
"""


last_name = "Smith"
count = 0
for letter in last_name:
    print(letter, ' ', count)  # note a space between ' '
    count += 1


print('---and the second loop----')
count = 0
while count < 5:
    print(last_name[count], ' ', count)
    count += 1



