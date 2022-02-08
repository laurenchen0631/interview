class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]

s = Solution()
print(s.change(amount = 5, coins = [1,2,5]))
print(s.change(amount = 3, coins = [2]))
print(s.change(amount = 10, coins = [10]))