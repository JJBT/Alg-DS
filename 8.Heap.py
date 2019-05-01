"""Куча - структура данных над деревом. Поддерживает:
Минимальный элемент (Будет корнем дерева)
Вставка и удаление - O(log n)
Инвариант: x.val >= x.par.val"""


class Heap:
    """Heap on array"""
    A = []

    @staticmethod
    def parent(i):
        return (i + 1)//2 - 1

    @staticmethod
    def left_child(i):
        return 2*i + 1

    @staticmethod
    def right_child(i):
        return 2*i + 2

    def heaptify_up(self, i):
        """Поддержание справедливости инварианта"""
        if i > 0:
            j = self.parent(i)
            if self.A[i] < self.A[j]:
                self.A[i], self.A[j] = self.A[j], self.A[i]  # swapping
                self.heaptify_up(j)

    def heaptify_down(self, i):
        if self.left_child(i) < len(self.A) or self.right_child(i) < len(self.A):
            j = min(self.A[self.left_child(i)], self.A[self.right_child(i)])
            if self.A[i] > self.A[j]:
                self.A[i], self.A[j] = self.A[j], self.A[i]  # swapping
                self.heaptify_down(j)

