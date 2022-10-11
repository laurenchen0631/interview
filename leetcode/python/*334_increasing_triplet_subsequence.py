import sys


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        firstMin = secondMin = sys.maxsize
        for n in nums:
            if n <= firstMin:
                firstMin = n
            elif n <= secondMin:
                secondMin = n
            else:
                return True
        return False

s = Solution()
print(s.increasingTriplet([1, 2, 3, 4, 5]))
print(s.increasingTriplet([2,1,5,0,4,6]))
print(s.increasingTriplet([5,4,3,2,1]))
print(s.increasingTriplet([1,1,1,1]))