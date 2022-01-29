class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i): # left tree nodes
                dp[i] += dp[j] * dp[i-1-j]
        return dp[-1]

s = Solution()
print(s.numTrees(1))
print(s.numTrees(2))
print(s.numTrees(3))
print(s.numTrees(4))
print(s.numTrees(5))
print(s.numTrees(6))