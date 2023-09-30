class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        res: int = 0
        i = 0
        while i < len(nums):
            cur = 1
            while i + 1 < len(nums) and nums[i] < nums[i+1]:
                cur += 1
                i += 1
            
            i += 1
            res += cur * (cur+1) // 2
        return res