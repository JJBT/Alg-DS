class FastArray:
    A = list()
    B = list()  # на i позиции хранить порядковый номер, под которым была инициализирована ячейка i
    C = list()  # на i позиции хранить номер ячейки, которая была проинициализирована i по счету
    k = int()  # счетчик инициализированных ячеек

    def __init__(self, n):
        self.k = 0

    def is_inited(self, i):
        if (len(self.B) < i + 1) and (len(self.C) < i + 1):
            return False
        return 0 < self.B[i] <= self.k and self.C[self.B[i]] == i

    def read(self, i):
        """O(1)"""
        if self.is_inited(i):
            return self.A[i]
        else:
            return 0

    def write(self, i, v):
        """!!!!Предполагается что массив заполняется по порядку.
        O(1)"""
        self.A.insert(i, v)
        if not self.is_inited(i):
            self.k += 1
            self.B.insert(i, self.k)
            self.C.insert(self.k, i)

    def display(self):
        print(self.A)
        print(self.B)
        print(self.C)


o = FastArray(10)
o.display()
o.write(0, 7)
o.display()
print(o.read(4))
print(o.read(5))


class Stack:
    def __init__(self, *args):
        self.__a = []
        for i in args:
            self.__a.append(i)

    def pop(self):
        self.__a.pop()

    def push(self, value):
        self.__a.append(value)

    def display(self):
        for i in reversed(self.__a):
            print(i)

