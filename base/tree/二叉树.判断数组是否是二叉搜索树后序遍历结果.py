# -*- encoding: utf-8 -*-
# 数组是否是二叉搜索树后序遍历结果


def is_bst(a, left, right):
    if right <= left:
        return True
    root = a[right]
    middle = a[left]
    for i in range(left, right):
        if a[middle] >= a[root]:
            middle = i
            break
    for i in range(middle, right):
        if a[i] < a[root]:
            return False
    return is_bst(a, left, middle - 1) and is_bst(a, middle, right - 1)
