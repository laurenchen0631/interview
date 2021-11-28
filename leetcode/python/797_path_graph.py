class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res: list[list[int]] = []
        self.helper(graph, 0, [0], res)
        return res

    def helper(self, graph: list[list[int]], cur: int, path: list[int], res: list[list[int]]) -> None:
        end = len(graph) - 1
        neighbors = graph[cur]
        for n in neighbors:
            if n == end:
                res.append(path.copy())
            else:
                self.helper(graph, n, path, res)
            path.pop()


if __name__ == '__main__':
  s = Solution()
  print(s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
  print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))
  print(s.allPathsSourceTarget([[1],[]]))
  print(s.allPathsSourceTarget([[1,2,3],[2],[3],[]]))
  print(s.allPathsSourceTarget([[1,3],[2],[3],[]]))
  # print(s.allPathsSourceTarget("()()"))