class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        m = len(target)
        n = len(words[0])
        cnt = [[0] * n for _ in range(26)]
        for k in range(n):
            for word in words:
                cnt[ord(word[k]) - ord('a')][k] += 1
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(m + 1):
            for k in range(n):
                if i < m:
                    key = ord(target[i]) - ord('a')
                    dp[i + 1][k + 1] += (cnt[key][k] * dp[i][k])
                dp[i][k + 1] += dp[i][k]
        return dp[m][n]
    
s = Solution()
print(s.numWays(["acca","bbbb","caca"], "ab"))