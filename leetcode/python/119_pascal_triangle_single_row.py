from this import d


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        dp = [1]
        for i in range(1, rowIndex+1):
            dp.append(1)
            for j in range(i-1, 0, -1):
                dp[j] = dp[j] + dp[j-1]
        return dp

s = Solution()
print(s.getRow(3))