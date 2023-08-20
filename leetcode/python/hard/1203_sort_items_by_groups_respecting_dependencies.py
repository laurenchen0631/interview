from collections import defaultdict


class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        m = self.assign_group(group, m)
        item_graph, item_indegree, group_graph, group_indegree = self.build_graph(n, m, group, beforeItems)
        
        item_order = self.topological_sort(item_graph, item_indegree)
        if not item_order:
            return []
        group_order = self.topological_sort(group_graph, group_indegree)
        if not group_order:
            return []
    
        ordered_group = defaultdict(list[int])
        for i in item_order:
            ordered_group[group[i]].append(i)
        
        res = []
        for i in group_order:
            res.extend(ordered_group[i])
        return res

    def assign_group(self, group: list[int], m: int) -> int:
        for i, g in enumerate(group):
            if g == -1:
                group[i] = m
                m += 1
        return m
    
    def build_graph(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]):
        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n
        group_graph = [[] for _ in range(m)]
        group_indegree = [0] * m
        
        for v in range(n):
            for u in beforeItems[v]:
                item_graph[u].append(v)
                item_indegree[v] += 1
                
                if (gu := group[u]) != (gv := group[v]):
                    group_graph[gu].append(gv)
                    group_indegree[gv] += 1
                
        return item_graph, item_indegree, group_graph, group_indegree
    
    def topological_sort(self, graph: list[list[int]], indegree: list[int]) -> list[int]:
        n = len(graph)
        order = []
        stack = [i for i in range(n) if indegree[i] == 0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    stack.append(v)
        return order if len(order) == n else []