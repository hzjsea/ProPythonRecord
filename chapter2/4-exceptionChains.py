#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: 4-exceptionChains.py.py
@time: 2021/2/19 10:21 上午
"""


# def get_value(dictionary, name):
#     try:
#         return dictionary[name]
#     except Exception as e:
#         print("exception hit..writing to file")
#         log = open('../temp/log.txt', 'w')
#         log.write('%s\n' % e)
#         log.close()
#
#
# names = {"jack": 12, "rose": 13}
# get_value({}, 'test')
#


# def validate(value, validator):
#     try:
#         return validator(value)
#     except Exception as e:
#         raise ValueError('Invalid value: %s' % value) from e
#
#
# def validator(value):
#     if len(value) > 10:
#         raise ValueError("Value can't exceed 10 characters")
#
#
# if __name__ == '__main__':
#     validate('test', validator)
#     validate(False, validator)


import logging


def count(file_name: str) -> int:

    file = None
    try:
        file = open(file_name, 'r')
        lines = file.readlines()
    except EnvironmentError as e:
        logging.error(e)
        return 0
    except TypeError as e:
        logging.error(e)
        return 0
    except UnicodeDecodeError as e:
        "The contents of the file were in an unknown encoding"
        logging.error(e)
        return 0
    else:
        return len(lines)
    finally:
        if file:
            file.close()
