from collections import deque


class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        g = [[] for i in range(n+1)]
        res = 0
        for u, v, dist in roads:
            g[u].append((v, dist))
            g[v].append((u, dist))
            res = max(res, dist)
        
        visited = set[int]()
        q = deque([1])
        while q:
            node = q.popleft()
            for neighbor, dist in g[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
                res = min(res, dist)
        return res
            