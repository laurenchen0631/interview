
from math import sqrt

class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        g = self.buildGraph(bombs)
        
        def dfs(node: int) -> int:
            stack = [node]
            visited = set()
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    stack.extend(g[node])
            return len(visited)
        
        return max(dfs(node) for node in g)
        
    def buildGraph(self, bombs: list[list[int]]) -> dict[int, list[int]]:
        g: dict[int, list[int]] = {i: [] for i in range(len(bombs))}
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                distance = sqrt((bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2)
                if distance <= bombs[i][2]:
                    g[i].append(j)
                if distance <= bombs[j][2]:
                    g[j].append(i)
                
        return g