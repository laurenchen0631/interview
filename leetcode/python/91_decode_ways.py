class Solution:
    def __init__(self):
        self.mappings = set[str]([str(i) for i in range(1, 27)])

    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1 if s[0] in self.mappings else 0
        for i in range(1, n):
            if s[i] in self.mappings:
                dp[i+1] += dp[i] 
            if s[i-1:i+1] in self.mappings:
                dp[i+1] += dp[i-1]
        return dp[n]
    
s = Solution()
print(s.numDecodings("12"))
print(s.numDecodings("1"))
print(s.numDecodings("226"))
print(s.numDecodings("11106"))
print(s.numDecodings("006"))
print(s.numDecodings("0"))
