class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        res = -1
        seen = [False] * len(edges)
        visiting = dict[int,int]()
        def dfs(node: int, i: int = 0) -> None:
            if seen[node]:
                return

            if node in visiting:
                nonlocal res
                res = max(res, i - visiting[node])
                return
            
            if edges[node] != -1:
                visiting[node] = i
                dfs(edges[node], i+1)
                visiting.pop(node)
            seen[node] = True
        for i in range(len(edges)):
            dfs(i)
        return res
        