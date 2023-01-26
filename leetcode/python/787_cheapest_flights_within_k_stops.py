import heapq
import sys


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        g = self.buildGraph(n, flights)
        heap = [(0, 0, src)]
        visited = [k+1] * n
        while heap:
            cost, depth, node = heapq.heappop(heap)
            if node == dst:
                return cost
            if depth >= visited[node]:
                continue
            visited[node] = depth
            for v, c in g[node]:
                heapq.heappush(heap, (cost + c, depth + 1, v))
        return -1
        
    def buildGraph(self, n: int, flights: list[list[int]]) -> list[list[tuple[int,int]]]:
        g = [[] for _ in range(n)]
        for u, v, cost in flights:
            g[u].append((v, cost))
        return g
    
s = Solution()
print(s.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
print(s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))