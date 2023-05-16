from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        if i < 0 or i >= self.n:
            return self.dummy
        if i < (self.n/2):
            p = self.dummy.next
            for j in range(i):
                p = p.next
        else:
            p = self.dummy
            for j in range(self.n-i):
                p = p.prev
        return p

    def get(self, i) -> object:
        if i < 0 or i >= self.n:
            raise IndexError
        return self.get_node(i).x

    def set(self, i: int, x: object) -> object:
        if i < 0 or i >= self.n:
            raise IndexError
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w: Node, x: object) -> Node:
        if w == None:
            raise IndexError
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        w.prev = u
        u.prev.next = u
        self.n = self.n + 1
        return u

    def add(self, i: int, x: object):
        if i < 0 or i > self.n:
            raise IndexError
        return self.add_before(self.get_node(i),x)

    def _remove(self, w: Node):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x

    def remove(self, i: int):
        if i < 0 or i >= self.n:
            raise IndexError
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        head = self.dummy.next
        tail = self.dummy.prev
        for k in range(self.n//2):
            if head.x != tail.x:
                return False
        head = head.next
        tail = tail.next
        return True

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def reverse(self):
        for i in range(self.n // 2):
            j = self.get(i)
            self.remove(i)
            self.add(i, self.get(self.n-i-1))
            self.remove(self.n-i-1)
            self.add(self.n-i, j)



    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
