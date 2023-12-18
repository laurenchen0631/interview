class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        first_min = second_min = 10001
        first_max = second_max = 0
        for n in nums:
            if n < first_min:
                second_min = first_min
                first_min = n
            elif n < second_min:
                second_min = n

            if n > first_max:
                second_max = first_max
                first_max = n
            elif n > second_max:
                second_max = n
        
        return first_max * second_max - first_min * second_min