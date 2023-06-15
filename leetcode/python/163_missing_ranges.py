class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        prev = lower - 1
        res: list[list[int]] = []
        for n in nums + [upper+1]:
            if n - prev >= 2:
                res.append([prev+1, n-1])
            prev = n
        return res

s = Solution()
print(s.findMissingRanges(nums = [0,1,3,50,75], lower = 0, upper = 99))