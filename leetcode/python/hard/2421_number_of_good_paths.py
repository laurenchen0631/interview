from collections import defaultdict
from math import comb


class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        res = n = len(vals)
        graph = {i: [] for i in range(n)}
        valNodes = defaultdict(set[int])
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            valNodes[vals[u]].add(u)
            valNodes[vals[v]].add(v)
        
        group: dict[int, int] = {}
        def union(u: int, v: int) -> None:
            group[find(u)] = find(v)
        def find(u: int) -> int:
            if u not in group:
                group[u] = u
            if group[u] != u:
                group[u] = find(group[u])
            return group[u]
        
        for v in sorted(valNodes.keys()):
            for node in valNodes[v]:
                for nei in graph[node]:
                    if vals[nei] <= v:
                        union(node, nei)
            groupCount = defaultdict(int)
            for node in valNodes[v]:
                groupCount[find(node)] += 1
            
            for count in groupCount.values():
                res += comb(count, 2)
        return res
        
s = Solution()
print(s.numberOfGoodPaths(vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]))