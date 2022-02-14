class Solution:
    def maxSumAfterOperation(self, nums: list[int]) -> int:
        dp = [0] * (len(nums)+1)
        dpOp = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            n = nums[i-1]
            dp[i] = max(dp[i-1]+n, n)
            dpOp[i] = max(dpOp[i-1]+n, max(dp[i-1], 0) + n*n)
        return max(dpOp)

s = Solution()
print(s.maxSumAfterOperation([2,-1,-4,-3]))
print(s.maxSumAfterOperation([1,-1,1,1,-1,-1,1]))