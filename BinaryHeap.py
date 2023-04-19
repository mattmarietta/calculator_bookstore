import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    return (2 * i + 1)


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    return (2 * (i + 1))


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    return ((i-1) // 2)


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        if len(self.a) == self.n:
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True

    def remove(self):
        if self.n == 0:
            raise IndexError
        x = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n = self.n - 1
        self._trickle_down_root()
        if (3 * self.n) < len(self.a):
            self._resize()
        return x

    def depth(self, u) -> int:
        if u == None:
            raise ValueError(f"{u} is not found in the binary tree.")
        for i in range(self.n):
            if self.a[i] == u:
                current_node = i
                d = 0
                while current_node != 0:
                    current_node = parent(current_node)
                    d += 1
                return d

    def height(self) -> int:
        return int(math.log2(self.n))

    def bf_order(self) -> list:
        return list(self.a[0:self.n])

    def in_order(self) -> list:
        return self._in_order(0)

    def _in_order(self, i):
        node = []
        if left(i) < self.n:
            node.extend(self._in_order(left(i)))
        node.append(self.a[i])
        if right(i) < self.n:
            node.extend(self._in_order(right(i)))
        return node

    def post_order(self) -> list:
        return self._post_order(0)

    def _post_order(self, i):
        node = []
        if left(i) < self.n:
            node.extend(self._post_order(left(i)))
        if right(i) < self.n:
            node.extend(self._post_order(right(i)))
        node.append(self.a[i])
        return node

    def pre_order(self) -> list:
        return self._pre_order(0)

    def _pre_order(self, i):
        node = []
        node.append(self.a[i])
        if left(i) < self.n:
            node.extend(self._pre_order(left(i)))
        if right(i) < self.n:
            node.extend(self._pre_order(right(i)))
        return node

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0:
            raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        i = self.n - 1
        p_idx = parent(i)
        while i > 0 and self.a[i] < self.a[p_idx]:
            temp = self.a[i]
            self.a[i] = self.a[p_idx]
            self.a[p_idx] = temp
            i = p_idx
            p_idx = parent(i)

    def _resize(self):
        f = _new_array(max(1, 2 * self.n))
        for i in range(0, self.n):
            f[i] = self.a[i % len(self.a)]
        self.a = f

    def _trickle_down_root(self):
        i = 0
        l_idx = left(i)
        r_idx = right(i)
        while i < self.n and (l_idx < self.n or r_idx < self.n) and (self.a[i] > self.a[l_idx] or self.a[r_idx] < self.a[i]):
            mini = min(self.a[i], self.a[l_idx], self.a[r_idx])
            if mini == self.a[l_idx]:
                min_idx = l_idx
            elif mini == self.a[r_idx]:
                min_idx = r_idx
            elif mini == self.a[i]:
                min_idx = i
            v = self.a[i]
            self.a[i] = self.a[min_idx]
            self.a[min_idx] = v
            ind = min_idx
            l_idx = left(ind)
            r_idx = right(ind)

    def __str__(self):
        return str(self.a[0:self.n])

    def printValues(self):
        print(f"in order = {self._in_order()}")
        print(f"bf order = {self.bf_order()}")
        print(f"post order = {self.post_order()}")
        print(f"")
