class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        res: int = 0
        for arr in grid:
            l = 0
            r = len(arr)
            while l < r:
                m = (l+r) // 2
                if arr[m] < 0:
                    r = m
                else:
                    l = m+1
            res += len(arr) - l
        return res

s = Solution()
print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(s.countNegatives([[3,2], [1,0]]))