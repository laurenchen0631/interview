from collections import defaultdict


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        g = self.buildGraph(equations, values)
        res: list[float] = []
        for [s, t] in queries:
            if s not in g or t not in g:
                res.append(-1.0)
            else:
                res.append(self.bfs(g, s, t))
        return res

    def buildGraph(self, path: list[list[str]], values: list[float]) -> dict[str, dict[str, float]]:
        g: dict[str, dict[str, float]] = defaultdict(dict[str, float])
        for i in range(len(path)):
            g[path[i][0]][path[i][1]] = values[i]
            g[path[i][1]][path[i][0]] = 1 / values[i]
        return g

    def bfs(self, g: dict[str, dict[str, float]], s: str, t: str) -> float:
        stack = [(s, 1.0)]
        visited = set[str]()

        while stack:
            (u, acc) = stack.pop()
            if u == t:
                return acc
            visited.add(u)
            for v in g[u].keys():
                if v not in visited:
                    stack.append((v, acc * g[u][v]))
        return -1.0

s = Solution()
print(s.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
print(s.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
print(s.calcEquation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]))
