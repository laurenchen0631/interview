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

    def minDistance(self, word1: str, word2: str) -> int:
        n = self.longestCommonSubsequence(word1, word2)
        return len(word1) + len(word2) - 2 * n

s = Solution()
print(s.minDistance(word1 = "sea", word2 = "eat"))
print(s.minDistance(word1 = "leetcode", word2 = "etco"))