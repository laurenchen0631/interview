from bisect import bisect_right


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(set(nums))
        res = n
        
        for i, l in enumerate(sorted_nums):
            r = l + n - 1
            j = bisect_right(sorted_nums, r)
            count = j - i
            res = min(res, n - count)
        
        return res