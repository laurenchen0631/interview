class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for n in coins:
            for i in range(n, amount+1):
                dp[i] = min(dp[i], dp[i-n]+1)

        return dp[amount] if dp[amount] != amount+1 else -1

s = Solution()
print(s.coinChange([1,2,5], 11))
print(s.coinChange([2], 3))
print(s.coinChange([1], 0))
print(s.coinChange([186,419,83,408], 6249))