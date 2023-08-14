class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        if len(nums) < 2:
            return False

        dp = [False] * (len(nums) + 1)
        dp[0] = True
        dp[2] = nums[0] == nums[1]
        for i in range(3, len(nums) + 1):
            if dp[i-2] and nums[i-1] == nums[i-2]:
                dp[i] = True
            elif dp[i-3] and nums[i-3] == nums[i-2] == nums[i-1]:
                dp[i] = True
            elif dp[i-3] and nums[i-3] + 1 == nums[i-2] and nums[i-2] + 1 == nums[i-1]:
                dp[i] = True
        return dp[-1]
            