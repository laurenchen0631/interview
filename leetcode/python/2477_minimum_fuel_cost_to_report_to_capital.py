from math import ceil


class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        g = [[] for _ in range(len(roads) + 1)]
        for u, v in roads:
            g[u].append(v)
            g[v].append(u)
        
        fuel = 0
        def dfs(node: int, parent: int) -> int:
            people = 1
            for child in g[node]:
                if child != parent:
                    people += dfs(child, node)
            nonlocal fuel
            if node != 0:
                fuel += ceil(people / seats)
            return people

        dfs(0, -1)
        return fuel
            