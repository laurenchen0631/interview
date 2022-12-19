class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        g = self.buildGraph(n, edges)
        q = [source]
        visited = set[int]()
        while q:
            tmp = []
            for i in q:
                if i == destination:
                    return True
                if i in visited:
                    continue
                visited.add(i)
                tmp.extend(g[i])
            q = tmp
        return False
        
    def buildGraph(self, n, edges):
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        return g