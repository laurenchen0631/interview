import math

class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        cur = res = 0

        for i, num in enumerate(nums, start=1):
            cur += num
            # At each step, we can try to minimize the element by evenly placing
            # the excess between the previous elements.
            res = max(math.ceil(cur / i), res)
            print(cur)

        return res

s = Solution()
# print(s.minimizeArrayValue([10, 1]))
print(s.minimizeArrayValue([3,7,1,6]))
# print(s.minimizeArrayValue([1,4,8,16]))
# print(s.minimizeArrayValue([1,4,8,16,12]))
# print(s.minimizeArrayValue([13,13,20,0,8,9,9]))
# print(s.minimizeArrayValue([6,9,3,8,14]))
# print(s.minimizeArrayValue([4,7,2,2,9,19,16,0,3,15]))