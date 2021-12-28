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

if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(s.minimumTotal([[-10]]))