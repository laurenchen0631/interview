from bisect import bisect_left

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        dp = [0] * (n+1)
        dp[-2] = 1
        starts = [e[0] for e in intervals]
        for i in range(n-2, -1, -1):
            j = bisect_left(starts, intervals[i][1])
            dp[i] = max(dp[i+1], 1+dp[j])
        return n - dp[0]

s = Solution()
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(s.eraseOverlapIntervals([[1,2],[2,3]]))
print(s.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))