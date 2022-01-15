class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for col in range(n-1, -1, -1):
            for row in range(m-1, -1, -1):
                if text2[col] == text1[row]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])
        return dp[0][0]

s = Solution()
print(s.longestCommonSubsequence(text1 = "abcde", text2 = "ace"))
print(s.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
print(s.longestCommonSubsequence(text1 = "abc", text2 = "def"))
