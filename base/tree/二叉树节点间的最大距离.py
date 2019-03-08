# -*- encoding: utf-8 -*-
#
from base.tree.Node import new_tree


def maxDistance(root):
    """
    二叉树节点间的最大距离
    :param root:
    :return: maxDistance, level
    """
    if not root:
        return 0, 0

    lMaxDistance, lLevel = maxDiatance(root.left)
    rMaxDistance, rLevel = maxDiatance(root.right)
    return max(lMaxDistance, rMaxDistance, lLevel + rLevel + 1), max(lLevel, rLevel) + 1


if __name__ == '__main__':
    tree = new_tree()
    diatance = maxDiatance(tree)
    print(diatance)
