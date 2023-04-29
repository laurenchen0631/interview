class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return
        
        if self.size[root_x] > self.size[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: list[list[int]], queries: list[list[int]]) -> list[bool]:
        sorted_queries = sorted([(w, u, v, i) for i, (u, v, w) in enumerate(queries)])
        edges = sorted([(w, u, v) for u, v, w in edgeList])
        
        uf = UnionFind(n)
        res = [False] * len(queries)
        i = 0
        for w, u, v, idx in sorted_queries:
            while i < len(edges) and edges[i][0] < w:
                _, x, y = edges[i]
                uf.union(x, y)
                i += 1
            
            res[idx] = uf.find(u) == uf.find(v)
        return res