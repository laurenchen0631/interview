from collections import deque


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        labels = [0] * n
        visited = set[int]()
        label: 1 | -1 = 1
        for s in range(n):
            if s in visited:
                continue
            q = deque([s, None])
            while q:
                u = q.popleft()
                if u == None:
                    label = -label
                    if q:
                        q.append(None)
                    continue
                visited.add(u)
                labels[u] = label
                for neighbor in graph[u]:
                    if neighbor not in visited:
                        q.append(neighbor)
        
        for u in range(n):
            for v in graph[u]:
                if labels[u] == labels[v]:
                    return False
        return True

s = Solution()
print(s.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
print(s.isBipartite([[1,3],[0,2],[1,3],[0,2]]))