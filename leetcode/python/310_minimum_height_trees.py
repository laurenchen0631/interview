class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n <= 2:
            return [i for i in range(n)]

        neighbors = self._transformEdges(edges)
        return self._findCentroids(neighbors)
        
    def _transformEdges(self, edges: list[list[int]]) -> list[set[int]]:
        neighbors = [set[int]() for _ in range(len(edges) + 1)]
        for [start, end] in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        return neighbors

    def _findCentroids(self, edges: list[set[int]]) -> list[int]:
        leaves: list[int] = []
        for (i, nodes) in enumerate(edges):
            if len(nodes) == 1:
                leaves.append(i)

        remaining = len(edges)
        while remaining > 2:
            remaining -= len(leaves)
            tmp: list[int] = []
            for leaf in leaves:
                parent = edges[leaf].pop()
                edges[parent].remove(leaf)
                if len(edges[parent]) == 1:
                    tmp.append(parent)
            leaves = tmp
        return leaves