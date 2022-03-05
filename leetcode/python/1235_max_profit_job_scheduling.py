from bisect import bisect_left


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))])
        dp = [0] * (len(jobs) + 1)
        starts = [jobs[i][0] for i in range(len(jobs))]

        for i in range(len(jobs)-1, -1, -1):
            nextJob = bisect_left(starts, jobs[i][1])
            dp[i] = max(dp[i+1], jobs[i][2] + dp[nextJob])

        return dp[0]

s = Solution()
print(s.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))
print(s.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]))

print(s.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]))