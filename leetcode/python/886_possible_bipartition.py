class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for u, v in dislikes:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        colors = [0] * n
        for i in range(n):
            if colors[i] == 0:
                colors[i] = 1
                stack = [i]
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        if colors[neighbor] == colors[node]:
                            return False
                        if colors[neighbor] == 0:
                            colors[neighbor] = -colors[node]
                            stack.append(neighbor)
        return True