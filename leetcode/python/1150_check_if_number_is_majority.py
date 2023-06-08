from bisect import bisect_left, bisect_right


class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        l = bisect_left(nums, target)
        r = bisect_right(nums, target)
        return r - l > len(nums) // 2