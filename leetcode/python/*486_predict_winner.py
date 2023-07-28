from functools import lru_cache


class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = nums[i]
            for j in range(i+1, n):
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][-1] >= 0
    
    def predictWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        
        @lru_cache()
        def maxDiff(l: int, r: int) -> int:
            if l == r:
                return nums[l]
            score_left = nums[l] - maxDiff(l+1, r)
            score_right = nums[r] - maxDiff(l, r-1)
            return max(score_left, score_right)
        
        return maxDiff(0, n-1) >= 0
        

s = Solution()
print(s.PredictTheWinner([1,5,2]))
print(s.PredictTheWinner([1,5,233,7]))
print(s.PredictTheWinner([1,5,2,4,6]))