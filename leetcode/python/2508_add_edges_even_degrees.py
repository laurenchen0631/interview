class Solution:
    def isPossible(self, n: int, edges: list[list[int]]) -> bool:
        g = self.buildGraph(n, edges)
        oddNodes = [i for i in range(1, n+1) if len(g[i]) % 2 == 1]
        evenNodes = [i for i in range(1, n+1) if len(g[i]) % 2 == 0]
        
        if len(oddNodes) not in {0, 2, 4}:
            return False

        if len(oddNodes) == 0:
            return True
        
        if len(oddNodes) == 2:
            if oddNodes[1] not in g[oddNodes[0]]: # not connected
                return True
            for v in evenNodes: # odds connect to the same even node
                if oddNodes[0] not in g[v] and oddNodes[1] not in g[v]:
                    return True
            return False
        
        a, b, c, d = oddNodes[0], oddNodes[1], oddNodes[2], oddNodes[3]
        if a not in g[b] and c not in g[d]:
            return True
        if a not in g[c] and b not in g[d]:
            return True
        if a not in g[d] and b not in g[c]:
            return True
        return False
            
        
        
    
    def buildGraph(self, n: int, edges: list[list[int]]) -> list[set[int]]:
        graph = [set() for _ in range(n+1)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        return graph

s = Solution()
print(s.isPossible(5, [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]))