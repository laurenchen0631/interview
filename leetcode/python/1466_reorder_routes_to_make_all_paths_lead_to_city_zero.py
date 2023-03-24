class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in connections:
            g[u].append((v, 1))
            g[v].append((u, 0))
        res = 0
        def dfs(node: int, parent: int):
            nonlocal res
            for neighbor, dist in g[node]:
                if neighbor != parent:
                    res += dist
                    dfs(neighbor, node)
        dfs(0, -1)
        return res