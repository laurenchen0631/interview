class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = nums[i]
            for j in range(i+1, n):
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][-1] >= 0

s = Solution()
print(s.PredictTheWinner([1,5,2]))
print(s.PredictTheWinner([1,5,233,7]))
print(s.PredictTheWinner([1,5,2,4,6]))