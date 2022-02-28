class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        i = 0
        res: list[str] = []
        while i < len(nums):
            start = end = nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1] - 1:
                i += 1
                end = nums[i]
            i += 1
            if start == end:
                res.append(str(start))
            else:
                res.append(f'{start}->{end}')
        return res

s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]))
print(s.summaryRanges([0,2,3,4,6,8,9]))