from calendar import c


class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        dp[-1][-1] = 1
        for i in range(len(s)-2, -1, -1):
            dp[i][i] = 1
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
            for j in range(i+2, len(s)):
                if s[i] == s[j] and dp[i+1][j-1] > 0:
                    dp[i][j] = 1
        
        return sum([sum(row) for row in dp])

s = Solution()
print(s.countSubstrings("abc"))
print(s.countSubstrings("aaa"))
print(s.countSubstrings("cabaccaca"))