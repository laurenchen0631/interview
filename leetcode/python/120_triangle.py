import sys
from numpy import tri


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [None] * len(triangle[-1])
        dp[0] = triangle[0][0]
        for layer in triangle[1:]:
            for i in range(len(layer) - 1, -1, -1):
                n = layer[i]
                if i == 0:
                    dp[i] = n + dp[i]
                elif i == len(layer) - 1:
                    dp[i] = n + dp[i-1]
                else:
                    dp[i] = min(dp[i-1] + n, dp[i] + n)
        return min(dp)

    def minimumTotalAlt(self, triangle: list[list[int]]) -> int:
        levels = len(triangle)
        if levels == 0:
            return 0
        dp = [sys.maxsize] * (levels+1)
        dp[1] = triangle[0][0]
        for l in range(1, levels):
            for i in range(l+1, 0, -1):
                dp[i] = triangle[l][i-1] + min(dp[i], dp[i-1])
        return min(dp[1:])
    

if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(s.minimumTotal([[-10]]))
    print(s.minimumTotalAlt([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(s.minimumTotalAlt([[-10]]))