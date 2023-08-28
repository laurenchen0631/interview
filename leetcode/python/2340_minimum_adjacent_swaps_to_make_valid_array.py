class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        min_index = max_index = 0
        for i, n in enumerate(nums):
            if n < nums[min_index]:
                min_index = i
            if n >= nums[max_index]:
                max_index = i
        
        return min_index + (len(nums) - 1 - max_index) - (1 if min_index > max_index else 0)