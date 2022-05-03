from pandas import array


class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        sortedNums = sorted(nums)
        while l <= r and sortedNums[l] == nums[l]:
            l += 1
        while  l <= r and sortedNums[r] == nums[r]:
            r -= 1
        return r - l + 1

s = Solution()
print(s.findUnsortedSubarray([2,6,4,8,10,9,15]))
print(s.findUnsortedSubarray([1,2,3,4]))
print(s.findUnsortedSubarray([1]))