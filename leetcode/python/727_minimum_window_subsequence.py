class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)
        # dp[i][j]: the closest start_index of S[:j] that contains T[:i] as a subsequence.
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = j # Case 0 (Intialize): empty string
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s2[i - 1] == s1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        # Look through last row, to find the minimun window
        minLen, start = len(s1)+1, -1
        for length in range(n + 1):
            if dp[m][length] != -1 and length - dp[m][length] < minLen:
                start, minLen = dp[m][length], (length - dp[m][length])
        return s1[start:start+minLen] if start != -1 else ''

s = Solution()
print(s.minWindow(s1 = "abcdebdde", s2 = "bde"))
# print(s.minWindow(s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"))
# print(s.minWindow("nkzcnhczmccqouqadqtmjjzltgdzthm", "bt"))