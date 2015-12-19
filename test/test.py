#!/usr/bin/env python
# -*- coding: utf-8 -*-


# n = int(input(">> "))
# result = []
# for i in range(n + 1):
#     lst = []
#     lst.extend(i * [i])
#     result.extend(lst)
#
# print(*result, sep=" ")

a = int(input(">> "))
result = []
for n in range(1, a + 1):
    seq = [n] * n      #  последовательность из n  n раз
    result.extend(seq) # добавить seq в результирующий список

print(*result, sep=" ")


