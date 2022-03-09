class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return str1+str2
        
        common = self.lcs(str1, str2)
        i = j = 0
        res: list[str] = []
        for c in common:
            while i < len(str1) and str1[i] != c:
                res.append(str1[i])
                i += 1
            while j < len(str2) and str2[j] != c:
                res.append(str2[j])
                j += 1
            res.append(c)
            i += 1
            j += 1

        return ''.join(res) + str1[i:] + str2[j:]

    def lcs(self, s1: str, s2: str) -> str:
        m = len(s1)
        n = len(s2)
        dp = [[''] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + s1[i-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1], key=len)
        return dp[-1][-1]

s = Solution()
print(s.shortestCommonSupersequence('bdacgla', 'eabkca'))
print(s.shortestCommonSupersequence(str1 = "abac", str2 = "cab"))