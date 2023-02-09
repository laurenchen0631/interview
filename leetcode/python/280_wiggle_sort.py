class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)-1):
            if (i & 1 == 0 and nums[i] > nums[i+1]) or (i & 1 == 1 and nums[i] < nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
            