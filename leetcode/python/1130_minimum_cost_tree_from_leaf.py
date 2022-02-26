import sys


class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        n = len(arr)
        dp = [[sys.maxsize] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        def partition(start: int, end: int) -> int:
            if dp[start][end] != sys.maxsize:
                return dp[start][end]
            for k in range(start, end):
                leftSubtotal = partition(start, k)
                rightSubtotal = partition(k+1, end)
                maxLeft = max(arr[start:k+1])
                maxRight = max(arr[k+1:end+1])
                dp[start][end] = min(dp[start][end], maxLeft*maxRight + leftSubtotal + rightSubtotal)
            return dp[start][end]
        return partition(0, n-1)

s = Solution()
print(s.mctFromLeafValues([6,2,4]))
print(s.mctFromLeafValues([4,11]))
print(s.mctFromLeafValues([2,3,4,1]))