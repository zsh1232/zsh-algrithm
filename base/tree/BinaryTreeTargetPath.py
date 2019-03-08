# -*- encoding: utf-8 -*-
# 二叉树的路径
#


def path(root, target):
    if root.val == target.val:
        return [root]
    if not root:
        return []

    leftPath = [] if not root.left else path(root.left, target)
    rightPath = [] if not root.right else path(root.right, target)

    finalPath = leftPath if len(leftPath) != 0 else rightPath
    if len(finalPath) != 0:
        return [root] + finalPath

    return []
