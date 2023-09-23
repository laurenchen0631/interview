class Solution:
    def validSubarrays(self, nums: list[int]) -> int:
        mono = []
        n = len(nums)
        right_index = [n]*n
        for i, v in enumerate(nums):
            while mono and v < nums[mono[-1]]:
                index = mono.pop(-1)
                right_index[index] = i
            mono.append(i)
        # can replace this loop by sum and arithmetic formula
        res = 0
        for i in range(len(nums)):
            res += right_index[i]-i
        return res 