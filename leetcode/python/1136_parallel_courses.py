from itertools import tee


class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        g, incoming = self.buildGraph(n, relations)
        res = 0
        visited = 0
        q = [i for i in range(n) if incoming[i] == 0]
        while q:
            res += 1
            tmp = []
            for u in q:
                visited += 1
                for v in g[u]:
                    incoming[v] -= 1
                    if incoming[v] == 0:
                        tmp.append(v)
            q = tmp
        return res if visited == n else -1

    def buildGraph(self, n: int, relations: list[list[int]]) -> tuple[list[list[int]], list[int]]:
        g = [[] for _ in range(n)]
        incoming = [0] * n
        for [u, v] in relations:
            g[u-1].append(v-1)
            incoming[v-1] += 1
        return g, incoming
        
s = Solution()
print(s.minimumSemesters(n = 3, relations = [[1,3],[2,3]]))
print(s.minimumSemesters(n = 3, relations = [[1,2],[2,3],[3,1]]))