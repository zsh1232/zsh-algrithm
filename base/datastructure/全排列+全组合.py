# -*- encoding: utf-8 -*-

def permute(a, i):
    """
    全排列
    :param a:
    :param i:
    :return:
    """
    if i == len(a):
        print(a)
    else:
        for j in range(i, len(a)):
            a[i], a[j] = a[j], a[i]
            permute(a, i + 1)
            a[i], a[j] = a[j], a[i]


# permute([1, 2, 3], 0)

def permuteHalf(a, m, i):
    """
    全排列
    :param a:
    :param i:
    :return:
    """
    if i == m:
        print(a[0:m])
    else:
        for j in range(i, len(a)):
            a[i], a[j] = a[j], a[i]
            permuteHalf(a, m, i + 1)
            a[i], a[j] = a[j], a[i]


permuteHalf(['a','b','c', 'd'], 1, 0)


def combanation(a, i, m, s):
    """
    组合公式
    :param a: 输入数组
    :param i: 第i个位置
    :param m: 收集m个元素
    :param s: 全局list, 收集组合结果
    :return:
    """
    if m == 0:
        print(s)
    elif i > len(a) - 1:
        return
    else:
        # 选择了第i个元素
        s.append(a[i])
        combanation(a, i + 1, m - 1, s)

        # 未选择第i个元素
        s.pop()
        combanation(a, i + 1, m, s)

# arr = [1, 2, 3]
# for i in range(1, len(arr) + 1):
#     combanation([1, 2, 3], 0, i, [])
