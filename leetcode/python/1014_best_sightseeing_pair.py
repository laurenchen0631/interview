class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        if len(values) == 0:
            return 0
        maximum: int = 0
        curMax: int = values[0]
        for n in values[1:]:
            curMax -= 1
            maximum = max(maximum, curMax + n)
            curMax = max(curMax, n)
        return maximum

s = Solution()
print(s.maxScoreSightseeingPair([8,1,5,2,6]))
print(s.maxScoreSightseeingPair([1,2]))
        