class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        total = sum(stones)
        dp = [[0] * (total // 2 + 1) for _ in range(len(stones) + 1)]
        for i in range(1, len(stones) + 1):
            for j in range(1, total // 2 + 1):
                if j >= stones[i-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j - stones[i-1]] + stones[i-1])
                else:
                     dp[i][j] = dp[i-1][j]
        return total - 2 * dp[-1][-1]

s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))
print(s.lastStoneWeight([31,26,33,21,40]))