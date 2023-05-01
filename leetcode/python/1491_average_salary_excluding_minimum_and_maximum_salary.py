class Solution:
    def average(self, salary: list[int]) -> float:
        total = curMax = 0
        curMin = 1e6
        for n in salary:
            total += n
            curMax = max(curMax, n)
            curMin = min(curMin, n)
        return (total - curMax - curMin) / (len(salary) - 2)