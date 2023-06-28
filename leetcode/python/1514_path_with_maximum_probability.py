import heapq


class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: List[float], start: int, end: int) -> float:
        g = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            g[u].append((v, succProb[i]))
            g[v].append((u, succProb[i]))
        
        heap = [(-1.0, start)] # max heap
        visited = [False] * n
        while heap:
            prob, node = heapq.heappop(heap)
            if node == end:
                return -prob
            if visited[node]:
                continue
            visited[node] = True
            for v, p in g[node]:
                if not visited[v]:
                    heapq.heappush(heap, (prob * p, v))
        return 0.0