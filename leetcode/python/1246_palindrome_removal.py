class Solution:
    def minimumMoves(self, arr: list[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if arr[i] == arr[j]:
                    dp[i][j] = max(dp[i+1][j-1], 1)
                else:
                    dp[i][j] = min(dp[i][k] + dp[k+1][j] for k in range(i, j))
        return dp[0][-1]

s = Solution()
# print(s.minimumMoves([1,2]))
# print(s.minimumMoves([1,3,4,1,5]))
print(s.minimumMoves([1,4,2,2,3,4,1]))
