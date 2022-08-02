class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        r = sum(nums)
        l: int = 0
        for i in range(len(nums)):
            r -= nums[i]
            if l == r:
                return i
            l += nums[i]
        return -1

s = Solution()
assert(s.pivotIndex(nums = [1,7,3,6,5,6]) == 3)
assert(s.pivotIndex(nums = [1,2,3]) == -1)
assert(s.pivotIndex(nums = [2,1,-1]) == 0)