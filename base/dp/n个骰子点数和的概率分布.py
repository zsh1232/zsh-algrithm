# -*- encoding: utf-8 -*-
# n个骰子点数和的概率分布.py


def probability(num, cub_max):
    """
    n个骰子点数和的概率分布
    :param num: 骰子个数
    :param cub_max: 骰子面数
    :return:
    """
    if num < 1:
        return

    # p是上一次结果, q是当前计算结果
    p, q = [0] * (cub_max * num + 1), [0] * (cub_max * num + 1)
    for i in range(1, cub_max + 1):
        p[i] = 1

    # 骰子数遍历
    for k in range(2, num + 1):
        for i in range(0, k):
            q[i] = 0

        # 点数遍历
        for i in range(k, k * cub_max + 1):
            q[i] = 0
            for j in range(1, cub_max + 1):
                if j <= i:
                    q[i] += p[i - j]

        # 最新的结果是p
        q, p = p, q

    # 概率
    for i in range(0, cub_max * num + 1):
        p[i] = str(p[i]) + "/" + str(cub_max * num)

    print(p)


if __name__ == '__main__':
    probability(2, 6)
