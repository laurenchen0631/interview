

import heapq
from math import inf


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        res = edges = 0
        visited = [False] * n
        
        dist = [inf] * n
        dist[0] = 0
        
        while edges < n:
            curMin = inf
            curNode = -1
            
            # Pick least weight node which is not in MST.
            for node in range(n):
                if not visited[node] and curMin > dist[node]:
                    curMin = dist[node]
                    curNode = node
            
            res += curMin
            edges += 1
            visited[curNode] = True
            
            # Update adjacent nodes of current node.
            for next in range(n):
                d = abs(points[curNode][0] - points[next][0]) + abs(points[curNode][1] - points[next][1])
                if not visited[next] and dist[next] > d:
                   dist[next] = d

        return res

s = Solution()
print(s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(s.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
print(s.minCostConnectPoints([[2,-3],[-17,-8],[13,8],[-17,-15]]))