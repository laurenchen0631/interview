class Solution:
    def jump(self, nums: list[int]) -> int:
        dp = [len(nums)+1] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                dp[j] = min(dp[j], dp[i]+1)
        return dp[-1]
    
s = Solution()
print(s.jump([2,3,1,1,4]))
print(s.jump([2,3,0,1,4]))