class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        dp = [[[False] * n for _ in range(n)] for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                for j in range(n - l + 1):
                    for k in range(1, l):
                        if (dp[k][i][j] and dp[l-k][i+k][j+k]) or (dp[k][i][j+l-k] and dp[l-k][i+k][j]):
                            dp[l][i][j] = True
                            break
        return dp[n][0][0]