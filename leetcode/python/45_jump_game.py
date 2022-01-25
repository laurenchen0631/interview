import sys
class Solution:
    def jump(self, nums: list[int]) -> int:
        dp = [sys.maxsize] * len(nums)
        dp[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                continue
            end = min(i + nums[i], len(nums) - 1)
            dp[i] = min(dp[j] for j in range(i+1, end+1)) + 1
        return dp[0]
    
s = Solution()
print(s.jump([2,3,1,1,4]))
print(s.jump([2,3,0,1,4]))