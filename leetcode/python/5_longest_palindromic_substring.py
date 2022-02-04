class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        dp = [[0] * n for _ in range(n)]
        length = 1
        start = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] != s[j]:
                    dp[i][j] = 0
                else: #s[i] == s[j]
                    if i < n-1 and j > i+1:
                        dp[i][j] = (dp[i+1][j-1] + 2) if dp[i+1][j-1] else 0
                    else: # base case: s[i] == s[i+1]
                        dp[i][j] = 2

                if dp[i][j] > length:
                    length = dp[i][j]
                    start = i
        
        return s[start:start+length]

s = Solution()
print(s.longestPalindrome("aa"))
print(s.longestPalindrome("abba"))
print(s.longestPalindrome("abaabbaa"))
print(s.longestPalindrome("aacabdkacaa"))
