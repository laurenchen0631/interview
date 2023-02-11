class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        g = self.buildGraph(n, redEdges, blueEdges)
        res = [-1] * n
        q = [(0, -1)]
        visited = {(0, 0), (0, 1)}
        depth = 0
        count = 0
        while q and count < n:
            tmp = []
            for i, color in q:
                if res[i] == -1:
                    res[i] = depth
                    count += 1
                for neighbor in g[i]:
                    if color != neighbor[1] and neighbor not in visited:
                        tmp.append(neighbor)
                        visited.add(neighbor)
            q = tmp
            depth += 1
        return res
        
    def buildGraph(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[list[tuple[int,int]]]:
        g: list[list[tuple[int,int]]] = [[] for _ in range(n)]
        for i, j in redEdges:
            g[i].append((j, 0))
        for i,j in blueEdges:
            g[i].append((j, 1))
        return g

s = Solution()
print(s.shortestAlternatingPaths(n = 3, redEdges = [[0,1],[1,2]], blueEdges = []))
print(s.shortestAlternatingPaths(n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]))
print(s.shortestAlternatingPaths(n = 5, redEdges = [[1,3], [3,4]], blueEdges = [[0,1], [1,2], [3,2], [3,3]]))