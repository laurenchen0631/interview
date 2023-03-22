class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        res = count = 0
        for n in nums:
            if n == 0:
                count += 1
                res += count
            else:
                count = 0
        return res