"""Quick sort:
    1. делим массив специальныи образом
    2. применяем алгоритм к каждой из частей рекурсивно
    Деление:
        на части, в каждой из которых все элементы либо больше или равны
        или меньше опорного элемента
    Эффективность зависит от выбора опорного элемента.
    Идеальный случай - медиана на каждом шаге -
    T(n) = T(n/2) + T(n/2) + O(n) = O(n*log n)"""


def Quick_sort(A, l, r):
    if l < r:
        q = Partition(A, l, r)
        Quick_sort(A, l, q)
        Quick_sort(A, q + 1, r)
    return A


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
        A[i], A[j] = A[j], A[i]  # swapping
        i += 1
        j -= 1
    return j


a = [6, 5, 4, 3, 2, 1]

print(Quick_sort(a, 0, len(a) - 1))