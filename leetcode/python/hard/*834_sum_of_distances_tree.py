class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        g = self.bulidGraph(n, edges)
        
        count = [1] * n
        ans = [0] * n
        def dfs(node: int, parent = None):
            for child in g[node]:
                if child == parent:
                    continue
                dfs(child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]
                
        def dfs2(node: int, parent = None):
            for child in g[node]:
                if child == parent:
                    continue
                ans[child] = ans[node] - count[child] + n - count[child]
                dfs2(child, node)
                
        dfs(0)
        print(count)
        print(ans)
        dfs2(0)
                
        return ans

    def bulidGraph(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        return g
    
s = Solution()
print(s.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))