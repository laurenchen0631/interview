class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[(0, '')] * n for _ in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j] and dp[i+1][j-1][1] != s[i]:
                    dp[i][j] = (dp[i+1][j-1][0] + 2, s[i])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1], dp[i+1][j-1], key=lambda e: e[0])
        return dp[0][n-1][0]

s = Solution()
print(s.longestPalindromeSubseq("bbabab"))
print(s.longestPalindromeSubseq("dcbccacdb"))