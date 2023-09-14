from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list[str])
        for u, v in tickets:
            graph[u].append(v)
        for _, dests in graph.items():
            dests.sort(reverse=True)
        
        res = []
        def dfs(node: str):
            while graph[node]:
                dfs(graph[node].pop())
            res.append(node)
        
        dfs('JFK')
        return res[::-1]