import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for [u, v, t] in times:
            graph[u].append((v, t))
        visited = set[int]()
        q = [(0, k)]
        total: int = 0
        while q:
            t, u = heapq.heappop(q)
            if u in visited:
                continue
            visited.add(u)
            total = max(total, t)
            for v, c in graph[u]:
                if v not in visited:
                    heapq.heappush(q, (t+c, v))
        return total if len(visited) == n else -1
            

s = Solution()
print(s.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(s.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
print(s.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
print(s.networkDelayTime([[1,2,1],[2,1,3]], 2, 2))
print(s.networkDelayTime([[2,4,10],[5,2,38],[3,4,33],[4,2,76],[3,2,64],[1,5,54],[1,4,98],[2,3,61],[2,1,0],[3,5,77],[5,1,34],[3,1,79],[5,3,2],[1,2,59],[4,3,46],[5,4,44],[2,5,89],[4,5,21],[1,3,86],[4,1,95]], 5, 1))