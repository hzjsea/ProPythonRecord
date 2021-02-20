#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: 10-Named Tuple.py
@time: 2021/2/20 10:23 上午
"""

from collections import namedtuple

Point = namedtuple("Point", 'x y')
point = Point(13, 25)
print(point) # Point(x=13, y=25)
print(point.x)
print(point.y)


from collections import OrderedDict
d = OrderedDict((value, str(value))for value in range(10) if value > 1)
print(d)  # OrderedDict([(2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')])


dd = dict((value, str(value)) for value in range(10) if value > 1)
print(dd)  # {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


dict = {"name": "hzj", "age": 12}
print(dict.get("name"))  # hzj
print(dict.get("address", "hangzhou"))  # hangzhou


def count_words(text):
    count = {}
    for word in text.split(' '):
        current = count.get(word, 0)
        count[word] = current + 1
    return count


print(count_words("a b bcb bdsb adabdbcvbs dsb ca a"))
# {'a': 2, 'b': 1, 'bcb': 1, 'bdsb': 1, 'adabdbcvbs': 1, 'dsb': 1, 'ca': 1}


from collections import defaultdict


def count_words2(text):
    count = defaultdict(int)
    for word in text.split(' '):
        count[word] += 1
    return count


print(count_words2("a b bcb bdsb adabdbcvbs dsb ca a"))
# defaultdict(<class 'int'>, {'a': 2, 'b': 1, 'bcb': 1, 'bdsb': 1, 'adabdbcvbs': 1, 'dsb': 1, 'ca': 1})