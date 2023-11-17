class Solution:
    # [1, 50, 60, 100]
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        res = nums[0] + nums[-1]
        for i in range(len(nums) // 2):
            res = max(res, nums[i] + nums[-i - 1])
        return res
