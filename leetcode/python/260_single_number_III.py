class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        for num in nums:
            xor ^= num
        mask = 1
        while xor & mask == 0:
            mask <<= 1
        num1 = 0
        num2 = 0
        for num in nums:
            if num & mask == 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]
