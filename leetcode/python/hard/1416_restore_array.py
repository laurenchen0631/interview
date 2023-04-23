class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(n):
            if s[i] == '0':
                continue
            
            for j in range(i, n):
                num = int(s[i:j+1])
                if num > k:
                    break
                dp[j+1] = (dp[j+1] + dp[i]) % (10**9 + 7)
        return dp[-1]