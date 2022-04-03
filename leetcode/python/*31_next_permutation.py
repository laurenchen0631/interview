class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i > -1 and nums[i] >= nums[i+1]:
            i -= 1
        if i > -1:
            j = len(nums) - 1
            while j > 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i+1, len(nums) - 1)
    
    def reverse(self, nums: list[int], i: int, j: int) -> None:
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

s = Solution()
print(s.nextPermutation([1, 1]))