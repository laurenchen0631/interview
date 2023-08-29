import math


class Solution:
    def minimumTime(self, jobs: list[int], workers: list[int]) -> int:
        jobs.sort()
        workers.sort()

        res = math.ceil(jobs[0] / workers[0])
        for needed, hour in zip(jobs, workers):
            res = max(res, math.ceil(needed / hour))
        return res
        