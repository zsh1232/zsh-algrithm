# -*- encoding: utf-8 -*-
# 1. 荷兰国旗问题
# 2. 找到第k大数
# 3. 奇数排在偶数前面


def sort_colors(a):
    """
    荷兰国旗问题
    :param a:
    :return:
    """
    i, k = -1, len(a)
    j = 0
    while j < k:
        if a[j] == 1:
            j += 1
        elif a[j] == 0:
            i += 1
            a[i], a[j] = a[j], a[i]
            j += 1
        else:
            k -= 1
            a[j], a[k] = a[k], a[j]


if __name__ == '__main__':
    arr = [0, 2, 1, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 2, 2]
    sort_colors(arr)
    print(arr)
