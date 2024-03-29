class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[n] * n for _ in range(n)]
        for size in range(1, n+1):
            for l in range(n - size + 1):
                r = l + size - 1
                j = -1
                for i in range(l, r):
                    if s[i] != s[r] and j == -1:
                        j = i
                    if j != -1:
                        dp[l][r] = min(dp[l][r], 1 + dp[j][i] + dp[i + 1][r])
                if j == -1:
                    dp[l][r] = 0
        return dp[0][-1] + 1