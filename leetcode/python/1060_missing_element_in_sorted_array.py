class Solution:
    def missingElement(self, nums: list[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        def count_missing(l: int, r: int) -> int:
            return (nums[r] - nums[l] - 1) - (r - l - 1)

        while l < r:
            m = (l + r + 1) // 2 # ceiling
            n = count_missing(l, m)
            if k > n:
                l = m
                k -= n
            else:
                r = m - 1
        return nums[l] + k