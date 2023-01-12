class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        g = {i: [] for i in range(n)}
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        res = [0] * n
        def dfs(node: int, parent: int, cnt: dict[str, int]) -> None:
            label = labels[node]
            if not g[node]:
                cnt[label] = cnt.get(label, 0) + 1
                res[node] = 1
                return
            old = cnt.copy()
            for child in g[node]:
                if child == parent:
                    continue
                dfs(child, node, cnt)
            cnt[label] = cnt.get(label, 0) + 1
            res[node] = cnt[label] - old.get(label, 0)
        dfs(0, -1, {})
        return res
    
s = Solution()
print(s.countSubTrees(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"))
print(s.countSubTrees(n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"))
print(s.countSubTrees(n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"))