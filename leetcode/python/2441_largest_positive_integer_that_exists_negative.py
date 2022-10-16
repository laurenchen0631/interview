import heapq


class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        numSet = set(nums)
        sortedNums = sorted(nums, reverse=True)
        for n in sortedNums:
            if -n in numSet:
                return n
        return -1

s = Solution()
print(s.findMaxK([-10,8,6,7,-2,-3]))
print(s.findMaxK([-1,2,-3,3]))
print(s.findMaxK([-1,10,6,7,-7,1]))
