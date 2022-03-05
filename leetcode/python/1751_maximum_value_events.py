from bisect import bisect_left, bisect_right

class Solution:
    def maxEvents(self, events: list[list[int]], k: int) -> int:
        n = len(events)
        dp = [[0 for _ in range(k + 1)] for _ in range(n+1)]
        events.sort()
        starts = [x for x,_,_ in events]

        for i in range(n-1, -1, -1):
            for j in range(1, k+1):
                next_event = bisect_right(starts, events[i][1])
                dp[i][j] = max(dp[i+1][j], events[i][2] + dp[next_event][j-1])
        
        return dp[0][-1]
    

s = Solution()
# print(s.maxEvents(events = [[1,2,4],[3,4,3],[2,3,10]], k = 2))
# print(s.maxEvents(events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3))
# print(s.maxEvents([[11,17,56],[24,40,53],[5,62,67],[66,69,84],[56,89,15]], 2))
print(s.maxEvents([[19,42,7],[41,73,15],[52,73,84],[84,92,96],[6,64,50],[12,56,27],[22,74,44],[38,85,61]], 5))