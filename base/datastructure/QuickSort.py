# -*- encoding: utf-8 -*-
# 快速排序
#


def partition(a, left, right):
    if left < right:
        tmp = a[right]
        i = left - 1
        for j in range(left, right):
            if a[j] <= tmp:
                i = i + 1
                a[i], a[j] = a[j], a[i]

        a[i + 1], a[right] = a[right], a[i + 1]
        return i + 1


def quick_sort(a, left, right):
    if left < right:
        p = partition(a, left, right)
        quick_sort(a, left, p - 1)
        quick_sort(a, p + 1, right)


if __name__ == '__main__':
    a = [4, 3, 2, 5, 7, 1, 9]
    quick_sort(a, 0, len(a) - 1)
    print(a)

