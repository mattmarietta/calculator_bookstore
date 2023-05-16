from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np
"""An implementation of the adjacency list representation of a graph"""

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def add_edge(self, i : int, j : int):
        if not(0 <= i < self.n and 0 <= j < self.n):
            raise IndexError
        self.adj[i][j] = True

    def remove_edge(self, i : int, j : int):
        if not (0 <= i < self.n and 0 <= j < self.n):
            raise IndexError
        if self.adj[i][j] == False:
            return False
        self.adj[i][j] = 0
        return True

    def has_edge(self, i : int, j: int) ->bool:
        return self.adj[i][j]

    def out_edges(self, i) -> List:
        #initialize empty list edges
        if i < 0 or i >= self.n:
            raise IndexError()
        edges = []
        for j in range(self.n):
            if self.adj[i][j] == 1:
                edges.append(j)
        return edges

    def in_edges(self, j) -> List:
        edges = []
        for i in range(self.n):
            if self.adj[i][j] == 1:
                edges.append(i)
        return edges


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

    def size(self):
        return self.n