import heapq


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        heap = [(0, (0, 0))]
        visited = set[tuple[int, int]]()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(heights)
        n = len(heights[0])
        goal = (m-1, n-1)
        while heap:
            (curMin, pos) = heapq.heappop(heap)
            if pos in visited:
                continue
            if pos == goal:
                return curMin
            
            visited.add(pos)
            for dy, dx in dirs:
                y = pos[0] + dy
                x = pos[1] + dx
                if 0 <= x < n and 0 <= y < m:
                    diff = abs(heights[pos[0]][pos[1]] - heights[y][x])
                    heapq.heappush(heap, (max(curMin, diff), (y, x)))

s = Solution()
print(s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
print(s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
print(s.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))