# -*- encoding: utf-8 -*-
# 1 2 8 9
# 2 4 9 11
# 4 7 10 13
# 6 8 11 15
# 一个数组, 每行从左向右递增, 每列从上向下递增, 查找一个数


def find(a, target):
    """
    a[i,j]为右上角的值, 如果相等就找到, 如果a[i,j]>target j++, 如果a[i,j]<target i++
    :param a:
    :param target:
    :return:
    """
    i = 0
    j = len(a[0])
    rows = len(a)
    while i < rows and j >= 0:
        if target == a[i][j]:
            return True
        elif target > a[i][j]:
            j = j - 1
        else:
            i = i + 1
    return False
