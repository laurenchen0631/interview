from collections import defaultdict


class Solution:
    def checkContradictions(self, equations: list[list[str]], values: list[float]) -> bool:
        weights = defaultdict(lambda: defaultdict(lambda: 1.0))
        parents = {}
        def find(x: str):
            parents.setdefault(x, x)
            if parents[x] != x:
                y = find(parents[x])
                weights[x][y] = weights[x][parents[x]] * weights[parents[x]][y]
                parents[x] = y
            return parents[x]
        
        def union(x: str, y: str, w: float) -> bool:
            root_x, root_y = find(x), find(y)
            if root_x == root_y: # 
                expected = weights[x][root_x] * (1 / weights[y][root_y])
                return abs(w - expected) > 10 ** -5
            parents[root_x] = root_y
            weights[root_x][root_y] = w * weights[y][root_y] * (1 / weights[x][root_x])
            return False
        return any(union(u, v, w) for (u, v), w in zip(equations, values))