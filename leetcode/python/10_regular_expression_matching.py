class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*' and dp[0][j-2]:
                dp[0][j] = True

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    if p[j-2] != s[i-1] and p[j-2] != '.':
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-1] or dp[i-1][j] or dp[i][j-2]
                elif s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
        for r in dp:
            print(r)
        return dp[-1][-1]

s = Solution()
# print(s.isMatch(s = "aa", p = "a"))
# print(s.isMatch(s = "aa", p = "a*"))
# print(s.isMatch(s = "ab", p = ".*"))
# print(s.isMatch("aab", "c*a*b"))
print(s.isMatch("mississi", "mis*is*"))
# print(s.isMatch("aaa", "ab*a"))