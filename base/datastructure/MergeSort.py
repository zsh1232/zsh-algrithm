# -*- encoding: utf-8 -*-
# 归并排序
# tmp临时数组


def merge(a, tmp, left, mid, right):
    i, j, k = left, mid, 0
    while i <= mid - 1 and j <= right:
        if a[i] <= a[j]:
            tmp[k] = a[i]
            i += 1
        else:
            tmp[k] = a[j]
            j += 1
        k += 1
    while i <= mid - 1:
        tmp[k] = a[i]
        i, k = i + 1, k + 1
    while j <= right:
        tmp[k] = a[j]
        j, k = j + 1, k + 1
    for i in range(0, k):
        a[i + left] = tmp[i]


def merge_sort(a, tmp, left, right):
    if left < right:
        center = (left + right) // 2
        merge_sort(a, tmp, left, center)
        merge_sort(a, tmp, center + 1, right)
        merge(a, tmp, left, center + 1, right)


if __name__ == '__main__':
    a = [4, 3, 2, 5, 7, 1, 9]
    tmp = [None] * len(a)
    merge_sort(a, tmp, 0, len(a) - 1)
    print(a)
