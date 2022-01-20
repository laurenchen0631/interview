import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = self.findAvgAndMax(piles, h)
        while left < right:
            mid = (left + right) // 2
            hours: int = 0
            for n in piles:
                hours += math.ceil(n / mid)
            if hours <= h: # slow down
                right = mid
            else:
                left = mid + 1
        return left

    def findAvgAndMax(self, nums: list[int], amount: int) -> tuple[int, int]:
        total: int = 0
        maximum = 0
        for n in nums:
            total += n
            maximum = max(maximum, n)
        return math.ceil(total/amount), maximum

s = Solution()
print(s.minEatingSpeed([3,6,7,11], h = 8))
print(s.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(s.minEatingSpeed(piles = [30,11,23,4,20], h = 6))