class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        res = suffixSum = 0
        for n in satisfaction[::-1]:
            suffixSum += n
            if suffixSum <= 0:
                return res
            res += suffixSum
        return res