# -*- encoding: utf-8 -*-
# 二叉树全部数字相加
#


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def nextBase(num):
    return 10 ** len(str(num))


def travelSum(root, base):
    new_base = root.val+base*nextBase(root.val) #计算
    if not root.left and not root.right:    #叶子节点直接打印
        return new_base

    # 传下的值
    total = 0
    if root.left:
        total += travelSum(root.left, new_base)
    if root.right:
        total += travelSum(root.right, new_base)
    return total


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(10000000000)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(travelSum(root, 0))
