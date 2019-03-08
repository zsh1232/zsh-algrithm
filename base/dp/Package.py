# -*- encoding: utf-8 -*-
# 01背包问题
# https://www.cnblogs.com/darknightsnow/archive/2012/09/30/2709360.html
# 有n 种不同的物品，每个物品有两个属性，size 体积，value 价值，
# 现在给一个容量为 w 的背包，问最多可带走多少价值的物品。

# 01背包问题: 原始解法
def package_solution1(size, value, p_size, N):
    """
    01背包问题
    :param size: 体积
    :param value:  价值数组
    :param p_size: 背包大小
    :param N: 物品数量
    :return: 总价值
    """
    #  0 1 2 3 4 5 6 7 ... N
    #0 0 0 0 0 0 0 0 0 ... 0
    #1 0
    #2 0           f[i][j]
    #3 0
    f = [[0] * (p_size + 1)] * (N + 1)
    for i in range(1, N + 1):
        for j in range(1, p_size + 1):
            if size[i] <= j:
                f[i][j] = max(f[i - 1][j], f[i - 1][j - size[i-1]] + value[i-1])
            else:
                f[i][j] = f[i - 1][j]
    return f[N][p_size]


# 01背包问题: 优化解法

if __name__ == '__main__':
    pass
