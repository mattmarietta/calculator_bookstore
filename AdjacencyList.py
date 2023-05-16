"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i : int, j : int):
        # precondition 0 <= i or j < self.n
        if not (0 <= i < self.n and 0 <= j < self.n):
            raise IndexError
        if not self.has_edge(i, j):
            self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        if not (0 <= i < self.n and 0 <= j < self.n):
            raise IndexError
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        if not (0 <= i < self.n and 0 <= j < self.n):
            raise IndexError
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                return True
        return False

    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, i) -> List:
        incoming = []
        for k in range(self.n):
            if self.has_edge(k, i):
                incoming.append(k)
        return incoming

    def bfs(self, r : int):
        traversal = []
        seen = [False] * self.n
        q = ArrayQueue.ArrayQueue()

        q.add(r)
        traversal.append(r)
        seen[r] = True

        while len(q) != 0:
            current = q.remove()
            neighbors = self.out_edges(current)
            for j in neighbors:
                if seen[j] is False:
                    q.add(j)
                    traversal.append(j)
                    seen[j] = True
        return traversal

    def dfs(self, r : int):
        traversal = []
        sta = ArrayStack.ArrayStack()
        seen = [False] * self.n

        sta.push(r)

        while sta.n != 0:
            current = sta.pop()
            if not seen[current]:
                traversal.append(current)
                seen[current] = True
                neighbor = self.out_edges(current)
                for j in reversed(neighbor):
                    if not seen[j]:
                        sta.push(j)
        return traversal

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s

    def size(self):
        return self.n
    