class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            n = int(s[i-2:i])
            if n >= 10 and n <= 26:
                dp[i] += dp[i-2]
            
        return dp[-1]
    
s = Solution()
print(s.numDecodings("12"))
print(s.numDecodings("1"))
print(s.numDecodings("226"))
print(s.numDecodings("11106"))
print(s.numDecodings("006"))
print(s.numDecodings("0"))
