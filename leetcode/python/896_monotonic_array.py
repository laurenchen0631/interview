class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        is_increasing = nums[0] < nums[-1]
        for i in range(1, len(nums)):
            if is_increasing and nums[i-1] > nums[i]:
                return False
            elif not is_increasing and nums[i-1] < nums[i]:
                return False
        return True