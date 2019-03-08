# 一 排序

## 1.1 快排

```java
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
```



## 1.2 归并

```java
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
```



## 1.3 堆排

```java
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
```

