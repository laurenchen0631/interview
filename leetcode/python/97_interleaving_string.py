class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [False] * (len(s2) + 1)
        dp[0] = True
        for j in range(1, len(s2) + 1):
            if s2[j-1] == s3[j-1]:
                dp[j] = True
            else:
                break
        
        for i in range(1, len(s1) + 1):
            dp[0] = dp[0] and (s1[i-1] == s3[i-1])
            for j in range(1, len(s2) + 1):
                dp[j] = (dp[j-1] and s2[j-1] == s3[i+j-1]) or (dp[j] and s1[i-1] == s3[i+j-1])
        return dp[-1]

s = Solution()
print(s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
print(s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))