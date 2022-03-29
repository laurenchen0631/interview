class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n+1) for _ in range(n+1)]
        maximum: int = 0
        for i in range(1, n+1):
            for j in range(1, i):
                if s[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    maximum = max(maximum, dp[i][j])
        return maximum

s = Solution()
print(s.longestRepeatingSubstring("abbaba"))
# print(s.longestRepeatingSubstring("aabcaabdaab" ))
# print(s.longestRepeatingSubstring("aaabaabbbaaabaabbaabbbabbbaaaabbaaaaaabbbaabbbbbbbbbaaaabbabbaba"))