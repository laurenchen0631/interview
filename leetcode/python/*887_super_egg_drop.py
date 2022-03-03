class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[t][k] = the max floor we can get by t drops with k eggs
        dp = [[0] * (k+1) for _ in range(n+1)] 
        m = 0 # drop times
        while dp[m][k] < n:
            m += 1 
            for j in range(1, k+1):
                dp[m][j] = 1 + dp[m-1][j] + dp[m-1][j-1]
        for i in range(m+1):
            print(dp[i])
        return m

s = Solution()
print(s.superEggDrop(2, 9))
print(s.superEggDrop(3, 100))