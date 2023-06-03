class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        g = self.buildGraph(manager)
        res = 0
        q = [(headID, 0)]
        while q:
            tmp = []
            for i, t in q:
                res = max(res, t)
                if i in g:
                    for j in g[i]:
                        tmp.append((j, t + informTime[i]))
            q = tmp
        return res
    
    def buildGraph(self, manager: list[int]) -> dict[int, list[int]]:
        g = {}
        for i, m in enumerate(manager):
            if m == -1:
                continue
            if m not in g:
                g[m] = []
            g[m].append(i)
        return g