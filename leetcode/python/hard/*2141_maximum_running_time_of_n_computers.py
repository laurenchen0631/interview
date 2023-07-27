class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        batteries.sort()
        extra = sum(batteries[:-n])
        live = batteries[-n:]
        for i in range(1, n):
            if extra // i < live[i] - live[i-1]:
                return live[i-1] + extra // i
            extra -= (live[i] - live[i-1]) * i
        return live[-1] + extra // n