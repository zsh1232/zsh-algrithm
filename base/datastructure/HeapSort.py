# -*- encoding: utf-8 -*-
# 堆排序
# 1. 堆化
# 2. 最大堆创建
# 3. 堆排序

# 建立最大堆


def heapify(a, i, n):
    tmp = a[i]
    while True:
        child = 2 * i + 1
        if child + 1 < n and a[child + 1] > a[child]:
            child = child + 1
        if child < n and a[child] > a[i]:
            a[i] = a[child]
            i = child
        else:
            break
    a[i] = tmp


def heap_sort(a):
    for i in range(len(a) // 2, -1, -1):
        heapify(a, i, len(a))

    for i in range(len(a) - 1, -1, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, 0, i)


if __name__ == '__main__':
    arr = [3, 4, 2, 4, 6, 71, 1]
    print(arr)
    heap_sort(arr)
    print(arr)

