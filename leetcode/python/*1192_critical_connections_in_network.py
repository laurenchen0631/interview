class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        g, res = self.buildGraph(n, connections)
        groups = [None] * n
        self.dfs(g, groups, res, 0, 0)
        return list(map(lambda e: list(e), res))
    
    def buildGraph(self, n: int, edges: list[list[int]]) -> tuple[list[list[int]], set[tuple[int, int]]]:
        g = [[] for _ in range(n)]
        conns = set[tuple[int, int]]()
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            conns.add((min(u, v), max(u, v)))
        return g, conns
    
    def dfs(self, g: list[list[int]], groups: list[int | None], connections: set[tuple[int, int]], node: int, rank: int) -> int:
        if groups[node] != None:
            return groups[node]
        
        groups[node] = rank
        minRank = rank + 1

        for neighbor in g[node]:
            if groups[neighbor] != None and groups[neighbor] == rank - 1: # parent
                continue
            neighborRank = self.dfs(g, groups, connections, neighbor, rank + 1)
            if neighborRank <= rank and (e := (min(node, neighbor), max(node, neighbor))) in connections:
                connections.remove(e)
            minRank = min(minRank, neighborRank)
        return minRank
        

s = Solution()
print(s.criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]))
print(s.criticalConnections(n = 2, connections = [[0,1]]))
print(s.criticalConnections(n = 5, connections = [[0,1], [0,2], [0,3], [1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]))
print(s.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
