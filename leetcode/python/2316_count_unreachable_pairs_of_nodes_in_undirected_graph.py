class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        groups = []
        visited = set[int]()
        for i in range(n):
            if i in visited:
                continue
            groups.append(0)
            stack = [i]
            visited.add(i)
            while stack:
                u = stack.pop()
                visited.add(u)
                groups[-1] += 1
                for v in g[u]:
                    if v not in visited:
                        stack.append(v)
        res = 0
        subtotal = 0
        for k in groups:
            res += k * (n - subtotal - k)
            subtotal += k
                
        return res
    
s = Solution()