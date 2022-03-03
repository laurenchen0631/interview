class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[1] = 1
        self.helper(n, dp)
        print(dp)
    
    def helper(self, n: int, dp: list[int]) -> int:
        if dp[n] != float('inf'):
            return dp[n]
        for i in range(1, n+1):
            dp[n] = min(dp[n], 1 + max(i-1, self.helper(n-i, dp)))
        return dp[n]

s = Solution()
print(s.twoEggDrop(100))
