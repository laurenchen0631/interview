class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res: list[list[int]] = []
        self.dfs(graph, 0, [], res)
        return res
    
    def dfs(self, graph: list[list[int]], node: int, path: list[int], res: list[list[int]]) -> None:
        path.append(node)
        if node == len(graph) - 1:
            res.append(path.copy())
            path.pop()
            return
        
        for neighbor in graph[node]:
            self.dfs(graph, neighbor, path, res)
        path.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))
    print(s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))