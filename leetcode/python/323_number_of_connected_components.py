class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        g = self.buildGraph(n, edges)
        visited = set[int]()
        res: int = 0
        for i in range(n):
            if i in visited:
                continue
            res += 1
            stack = [i]
            while stack:
                p = stack.pop()
                if p in visited:
                    continue
                visited.add(p)
                for neighbor in g[p]:
                    stack.append(neighbor)
        return res
        
    def buildGraph(self, n: int, edges: list[list[int]]):
        g = {i: [] for i in range(n)}
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        return g