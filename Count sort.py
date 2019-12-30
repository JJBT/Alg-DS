def count_sort(arr, k):
    import numpy as np
    c = np.zeros(k + 1, dtype=np.int)
    for i in range(len(arr)):
        c[arr[i]] += 1
    pos = 0
    for number in range(k + 1):
        for i in range(c[number]):
            arr[pos] = number
            pos += 1


s = [2, 4, 1, 3, 8, 8, 6]

count_sort(s, max(s))
print(s)
