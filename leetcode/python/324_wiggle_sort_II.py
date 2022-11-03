import math
class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = math.ceil(len(nums) / 2)
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

s = Solution()
a = [1,5,1,1,6,4]
s.wiggleSort(a)
print(a)