from heapq import heappop, heapify


class MyList(list):
    def __lt__(self, other):
        return self[0] < other[0]


def merge_k_sorted_lists(arrs):
    """O(n*k*log(k))"""
    arr = []
    heap = []
    k = len(arrs)
    for i in range(k):
        heap.append(MyList([float('inf'), arrs[i].__iter__()]))

    for j in range(len(heap)):
        heap[j][0] = heap[j][1].__next__()
    heapify(heap)

    while len(heap) > 0:
        arr.append(heap[0][0])
        try:
            heap[0][0] = heap[0][1].__next__()
        except StopIteration:
            heappop(heap)

        heapify(heap)

    return arr
