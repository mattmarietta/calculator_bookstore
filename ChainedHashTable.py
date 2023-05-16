from Interfaces import Set
from DLList import DLList
import numpy as np


class ChainedHashTable(Set):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, d_type=DLList):
        self.d_type = d_type
        self.d = 1
        self.t = self.alloc_table(2 ** self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=object)
        for i in range(n):
            t[i] = self.d_type()
        return t

    def _hash(self, key: object) -> int:
        return self.z * hash(key) % (2 ** self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n

    def find(self, key: object) -> object:
        bin = self._hash(key)
        for i in range(self.t[bin].size()):
            if self.t[bin].get(i).key == key:
                return self.t[bin].get(i).value
        return None


    def add(self, key: object, value: object):
        if self.find (key) is not None:
            return False
        if self.n == len(self.t):
            self.resize()
        bin = self._hash(key)
        item = self.Node(key, value)
        self.t[bin].add(0, item)
        self.n += 1
        return True


    def remove(self, key: int) -> object:
        bin = self._hash(key)
        for i in range(self.t[bin].size()):
            if self.t[bin].get(i).key == key:
                b = self.t[bin].remove(i)
                self.n -= 1
                if len(self.t) > 3 * self.n:
                    self.resize()
                return b
        return None


    def resize(self):
        if self.n == len(self.t):
            self.d += 1
        else:
            self.d -= 1
        temp = self.alloc_table(2**self.d)
        for j in range(len(self.t)):
            for i in range(self.t[j].size()):
                bin = self._hash(self.t[j].get(i).key)
                temp[bin].add(0, self.t[j].get(i))
        self.t = temp

    def __str__(self):
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"
