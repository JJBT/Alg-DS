"""Разделяй и властвуй
    1. Деление. Задача делится на несколько меньших подзадач подобных исходной
    2. Решение. Каждая из подзадач решается рекурсивно.
    3. Слияние.
"""


def power(x, y):
    """Тривиальный алгоритм возведения в степень
    О(n^2*10^n)  n - число цифр в записи"""
    z = 1
    for i in range(1, y + 1):
        z *= x
    return z


def power2(x, y, p):
    """Быстрое возведение в степень по модулю
    Глубина рекурсии O(log y)"""
    if y == 0:
        return 1
    else:
        t = power2(x, y//2, p)
        if y % 2 == 0:
            return t**2
        else:
            return x*t**2


# TODO
def select(A, k):
    """Поиск k-ой порядковой статистики -
     Элемент стоящий на k-ом месте в отсортированном массиве"""
    left = 0
    right = len(A) - 1
    while True:
        mid = Partition(A, left, right)
        if mid == k:
            return A[mid]
        elif k < mid:
            right = mid
        else:
            k -= mid + 1
            left = mid + 1


def Partition(A, l, r):
    """Разделение массива
        Переупорядочивается относительно опорного элемента
        А - массив, l, r - границы разделяемой части"""
    v = A[(l + r)//2]
    i = l
    j = r
    while i <= j:
        while A[i] < v:
            i += 1
        while A[j] > v:
            j -= 1
        if i >= j:
            break
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    return j


a = [6, 5, 4, 3, 2, 1]

print(select(a, 5))
