#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: 3-cachingException.py
@time: 2021/2/19 9:51 上午
"""


# def count_lines(file_name: str) -> int:
#     try:
#         return len(open(file_name, "r").readlines())
#     except:
#         print('exception error reading the file or calculating lines!')
#         return 0
#
#
# my_file = input("Enter file to open:")
# print(count_lines(my_file))


# def count_lines(file_name: str) -> int:
#     try:
#         return len(open(file_name, "r").readlines())
#     except IOError:
#         print('exception error reading the file or calculating lines!')
#         return 0
#
#
# my_file = input("Enter file to open:")
# print(count_lines(my_file))


# 捕获多种异常

# def count_lines(file_name: str) -> int:
#     try:
#         return len(open(file_name, "r").readlines())
#     except EnvironmentError:
#         print('exception error reading the file or calculating lines!')
#         return 0
#
#
# my_file = input("Enter file to open:")
# print(count_lines(my_file))


# 捕获多种异常

# def count_lines(file_name: str) -> int:
#     try:
#         return len(open(file_name, "r").readlines())
#     except (EnvironmentError,TypeError):
#         print('exception error reading the file or calculating lines!')
#         return 0
#
#
# my_file = input("Enter file to open:")
# print(count_lines(my_file))


# 捕获异常同时赋值
# import logging
#
#
# def count_lines(file_name: str) -> int:
#     try:
#         return len(open(file_name, "r").readlines())
#     except (EnvironmentError,TypeError) as e:
#         print('exception error reading the file or calculating lines!')
#         logging.error(e)
#         return 0
#
#
# my_file = input("Enter file to open:")
# print(count_lines(my_file))


# 根据不同的错误类型做不同的对应处理
import logging


def count_lines(file_name: str) -> int:
    try:
        return len(open(file_name, "r").readlines())
    except TypeError as e:
        logging.error(e)
        return 0
    except EnvironmentError as e:
        logging.error(e.args[1]) # ERROR:root:No such file or directory
        logging.error(e.args)  # ERROR:root:(2, 'No such file or directory')
        return 0


my_file = input("Enter file to open:")
print(count_lines(my_file))
