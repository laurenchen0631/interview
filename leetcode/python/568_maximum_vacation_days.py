from math import inf

class Solution:
    def maxVacationDays(self, flights: list[list[int]], days: list[list[int]]) -> int:
        n = len(flights)
        k = len(days[0])
        dp = [-inf] * n
        dp[0] = 0
        for w in range(k):
            tmp = [-inf] * n
            for i in range(n):
                for j in range(n):
                    if flights[i][j] or i == j:
                        tmp[j] = max(tmp[j], dp[i] + days[j][w])
            dp = tmp
        return max(dp)

s = Solution()
print(s.maxVacationDays(flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]))
print(s.maxVacationDays(flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]))
print(s.maxVacationDays(flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]]))