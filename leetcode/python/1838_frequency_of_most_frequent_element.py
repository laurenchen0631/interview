class Solution:
    # [1,2,3, 50,51,52,53, 100,101,102,103,104], k = 10
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        needed = 0
        l = 0
        res = 1
        for r in range(1, len(nums)):
            needed += (nums[r] - nums[r-1]) * (r - l)
            while needed > k:
                needed -= nums[r] - nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res