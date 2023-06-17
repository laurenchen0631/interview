class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            res = s[i]
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if len(res) < j - i + 1:
                            res = s[i:j+1]
        return res

s = Solution()
print(s.longestPalindrome("aa"))
print(s.longestPalindrome("abba"))
print(s.longestPalindrome("abaabbaa"))
print(s.longestPalindrome("aacabdkacaa"))
