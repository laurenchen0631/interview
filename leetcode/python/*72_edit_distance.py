class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if not n or not m:
            return m + n
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for i in range(n+1):
            dp[0][i] = i
        
        for row in range(1, m+1):
            for col in range(1, n+1):
                l = dp[row-1][col]
                b = dp[row][col-1]
                lb = dp[row-1][col-1]
                if word1[row-1] == word2[col-1]:
                    dp[row][col] = 1 + min(l, b, lb - 1)
                else:
                    dp[row][col] = 1 + min(l, b, lb)
        return dp[-1][-1]

s = Solution()
print(s.minDistance(word1 = "horse", word2 = "ros"))
print(s.minDistance(word1 = "intention", word2 = "execution"))
print(s.minDistance(word1 = "apple", word2 = "appier"))
print(s.minDistance("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically"))