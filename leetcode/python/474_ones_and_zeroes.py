from typing import Counter

class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            counter = Counter(s)
            zeroes = counter.get('0', 0)
            ones = counter.get('1', 0)
            for i in range(m, zeroes-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], 1+dp[i-zeroes][j-ones])
        return dp[m][n]

s = Solution()
print(s.findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3))
print(s.findMaxForm(strs = ["10","0","1"], m = 1, n = 1))