class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.lcs(s, s[::-1])
    
    def lcs(self, s: str, p: str) -> int:
        m = len(s)
        n = len(p)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

s = Solution()
print(s.longestPalindromeSubseq("bbbab"))
print(s.longestPalindromeSubseq("abcdgcba"))
print(s.lcs( "abcde", "ace"))
print(s.lcs( "abc", "abc"))
print(s.lcs( "abc", "def"))