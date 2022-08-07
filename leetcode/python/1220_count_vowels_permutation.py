class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [1] * 5
        for _ in range(n-1):
            dp = [
                dp[1] + dp[2] + dp[4],
                dp[0] + dp[2],
                dp[1] + dp[3],
                dp[2],
                dp[2] + dp[3],
            ]
        return sum(dp) % (10**9 + 7)

s = Solution()
print(s.countVowelPermutation(1))
print(s.countVowelPermutation(2))
print(s.countVowelPermutation(5))