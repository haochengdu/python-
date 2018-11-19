#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/12 15:26
@Author  : TX
@File    : test_01.py
@Software: PyCharm
"""

# class Parent(object):
#     x = 1
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass
#
#
# print(Parent.x, Child1.x, Child2.x)  # 1,1,1
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)  # 1,2,1
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)  # 3,2,3


# A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))  # {'a': 1, 'b': 2, ....'e': 5}
# A1 = range(10)  # range(0,9)
# A2 = [i for i in A1 if i in A0]  # []
# A3 = [A0[s] for s in A0]  # [1,2,3,4,5]
# A4 = [i for i in A1 if i in A3]  # [1,2,3,4,5]
# A5 = {i: i * i for i in A1}  # {0:0,1:1,2:4.....,9:81}
# A6 = [[i, i * i] for i in A1]  # [[0,0], [1,1],[2,4],...,[9,81]]
# print(A0)
# print(A1)
# print(A2)
# print(A3)
# print(A4)
# print(A5)
# print(A6)


# l = []
# for i in range(10):
#     l.append({'num': i})
#     # print(id({'num': i}))
#     # print(l)
# print(l)
#
# l = []
# a = {'num': 0}
# for i in range(10):
#     a['num'] = i
#     l.append(a)
#     # print(id(a))
#     # print(l)
# print(l)
"""
原因是：字典是可变对象，在下方的 l.append(a)的操作中是把字典 a的引用传到列表 l 中，当后
续操作修改a['num']的值的时候，l 中的值也会跟着改变，相当于浅拷贝。
"""

# def read_in_chunks(file_path, chunk_size=1024 * 1024):
#     """
#     Lazy function (generator) to read a file piece by piece.
#     Default chunk size: 1M
#     You can set your own chunk size
#     """
#     with open(file_path, 'rb') as f:
#         while True:
#             chunk_data = f.read(chunk_size)
#             if not chunk_data:
#                 break
#             yield chunk_data
#
#
# with open('new_file.jpg', 'wb') as f:
#     for chunk in read_in_chunks('./fire_test_000491.jpg'):
#         f.write(chunk)






