# -*- encoding: utf-8 -*-
# 不能重建二叉树


def fillPosArray(a, ai, aj, b, bi, bj, c, ci, cj):
    """
    前序中序遍历, 获得后序遍历结果, index容易些错
    :param a:
    :param ai:
    :param aj:
    :param b:
    :param bi:
    :param bj:
    :param c:
    :param ci:
    :param cj:
    :return:
    """
    if ai > aj or bi > bj or ci > cj:
        return
    elif ai == aj and bi == bj and ci == cj and a[ai] == b[bi]:
        c[ci] = a[ai]
    else:
        val = a[ai]
        bmid = b.index(val)
        c[cj] = val
        left_length = bmid - bi
        right_length = bj - bmid
        # 左子树
        fillPosArray(a, ai + 1, ai + left_length, b, bi, bmid - 1, c, ci, ci + left_length - 1)
        # 右子树
        fillPosArray(a, aj - right_length + 1, aj, b, bmid + 1, bj, c, cj - right_length, cj-1)


if __name__ == '__main__':
    a = [1, 2, 4, 5, 3, 6, 7]
    b = [4, 2, 5, 1, 6, 3, 7]
    c = [None] * len(a)
    fillPosArray(a, 0, len(a)-1, b, 0, len(b)-1, c, 0, len(c)-1)
    print(c)
