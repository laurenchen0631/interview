from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        g = defaultdict(set[str])
        for u, v in zip(s1, s2):
            if u != v:
                g[u].add(v)
                g[v].add(u)
        
        cache: dict[str, str] = {}
        res = []
        
        def dfs(node: str) -> str:
            visited = set[str]()
            stack = [node]
            curMin = node
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                curMin = min(curMin, node)
                visited.add(node)
                stack.extend(g[node])
            for node in visited:
                cache[node] = curMin
            return curMin
        
        for c in baseStr:
            if c not in g:
                res.append(c)
            elif c in cache:
                res.append(cache[c])
            else:
                res.append(dfs(c))
        return ''.join(res)
    
s = Solution()
print(s.smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser"))
print(s.smallestEquivalentString(s1 = "hello", s2 = "world", baseStr = "hold"))
print(s.smallestEquivalentString(s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"))