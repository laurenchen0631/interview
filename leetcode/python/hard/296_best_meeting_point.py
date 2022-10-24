class Solution:
    def minTotalDistance(self, grid: list[list[int]]) -> int:
        rows: list[int] = []
        cols: list[int] = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        cols.sort()
        return self.minManhattanDist(rows) + self.minManhattanDist(cols)

        
    def minManhattanDist(self, nums: list[int]):
        p = nums[len(nums) // 2]
        return sum([abs(n - p) for n in nums])

s = Solution()
print(s.minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]))