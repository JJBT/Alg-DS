def Insertion_sort(A):
    """Сортировка вставками"""
    """Teta(n^2) Смотрим каждый i элемент и ищем его место среди первых i-1 элементов"""
    n = len(A)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if A[j - 1] <= A[j]:
                break
            else:
                A[j - 1], A[j] = A[j], A[j - 1]
    return A


a = [6, 5, 4, 3, 1, 2, 1]
print(Insertion_sort(a))


"""Сортировка слиянием"""


def merge(A, B):
    """Слияние двух отсортированных массивов в один
    Teta(len(A) + len(B)))"""
    i = 0
    j = 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    C += A[i:len(A)] + B[j:len(B)]
    return C


def Merge_sort(A):
    """Сортировка слиянием
    Teta(n*log n)
    T(n) = 2T(n/2) + O(n)"""
    if len(A) < 2:
        return A
    else:
        n = len(A)
        A1 = Merge_sort(A[0:n//2])
        A2 = Merge_sort(A[n//2:n])
        return merge(A1, A2)


b = [3, 1, 2, 7, 8, 3, 4, 5, 2, 8, 3]
print(Merge_sort(b))

