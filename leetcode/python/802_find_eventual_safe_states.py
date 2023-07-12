from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        outgoing = [0] * n
        adj = [[] for _ in range(n)]
        for u, links in enumerate(graph):
            outgoing[u] = len(links)
            for v in links:
                adj[v].append(u)
        q = deque([u for u in range(n) if outgoing[u] == 0])
        safe = [False] * n
        while q:
            u = q.popleft()
            safe[u] = True
            for v in adj[u]:
                outgoing[v] -= 1
                if outgoing[v] == 0:
                    q.append(v)
        return [i for i in range(n) if safe[i]]