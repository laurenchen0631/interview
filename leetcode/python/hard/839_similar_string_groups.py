class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        n = len(strs)
        g = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if self.isSimilar(strs[i], strs[j]):
                    g[i].append(j)
                    g[j].append(i)
        groups = 0
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                groups += 1
                self.dfs(g, i, visited)
        return groups

    def isSimilar(self, s1: str, s2: str) -> bool:
        n = len(s1)
        cnt = 0
        for i in range(n):
            if s1[i] != s2[i]:
                cnt += 1
            if cnt > 2:
                return False
        return True
    
    def dfs(self, g: list[list[int]], i: int, visited: list[bool]) -> None:
        visited[i] = True
        for j in g[i]:
            if not visited[j]:
                self.dfs(g, j, visited)