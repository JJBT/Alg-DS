import math


def MEDIAN(A):
    """Алгоритм поиска медианы,
    A - массив"""
    """Худший случай: медиана на последнем месте - 
    n итераций внешнего цикла - n внутреннего
    Сложность Teta(n^2)"""
    n = len(A)
    for i in range(n):
        l = 0  # кол-во элементов в массиве больше чем выбранный
        g = 0  # кол-во элементов в массиве меньше чем выбранный
        for j in range(n):
            if A[j] < A[i]:
                l += 1
            elif A[j] > A[i]:
                g += 1
        if l <= n/2 and g <= n/2:
            return A[i]


def median(a):
    """Сложность = сложности сортировки"""
    n = len(a)
    B = sorted(a)
    return B[math.floor(n/2)]


a = [4, 5, 8, 3, 1]

print(MEDIAN(a))
print(median(a))

