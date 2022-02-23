class Solution:
    def shortestDistanceColor(self, colors: list[int], queries: list[list[int]]) -> list[int]:
        dp = [
            [len(colors)+1] * (len(colors) + 2), # 1
            [len(colors)+1] * (len(colors) + 2), # 2
            [len(colors)+1] * (len(colors) + 2), # 3
        ]
        for i in range(1, len(colors)+1):
            c = colors[i-1]
            for k in range(1, 4):
                dp[k-1][i] = (1 + dp[k-1][i-1]) if c != k else 0
        for i in range(len(colors), 0, -1):
            c = colors[i-1]
            for k in range(1, 4):
                dp[k-1][i] = min(dp[k-1][i], 1 + dp[k-1][i+1])
        res: list[int] = []
        for i, color in queries:
            if dp[color-1][i+1] >= len(colors) + 1:
                res.append(-1)
            else:
                res.append(dp[color-1][i+1])
        return res

s = Solution()
# print(s.shortestDistanceColor(colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]))
print(s.shortestDistanceColor(colors = [1,2], queries = [[0,3]]))