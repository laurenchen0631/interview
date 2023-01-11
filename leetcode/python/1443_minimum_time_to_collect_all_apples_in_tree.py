class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        g = {i: [] for i in range(n)}
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        def dfs(parent: int, node: int) -> int:
            res = 0
            for child in g[node]:
                if child == parent:
                    continue
                childTime = dfs(node, child)
                if childTime or hasApple[child]:
                    res += childTime + 2
            return res
        return dfs(-1, 0)