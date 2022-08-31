class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set[tuple[int, int]](), set[tuple[int, int]]()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(i: int, j: int, visited: set[tuple[int, int]]()) -> None:
            stack: list[tuple[int, int]] = [(i, j)]
            while stack:
                p = stack.pop()
                visited.add(p)
                for dy, dx in dirs:
                    y, x = p[0] + dy, p[1] + dx
                    if 0 <= y < m and 0 <= x < n and (y, x) not in visited and heights[y][x] >= heights[p[0]][p[1]]:
                        stack.append((y, x))
        
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)

        return list(map(list, pacific & atlantic))

s = Solution()
print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))