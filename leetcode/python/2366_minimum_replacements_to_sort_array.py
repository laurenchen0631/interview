class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                continue

            # 7 3 -> 2, 2, 3, 3
            needed_splits = (nums[i] + nums[i+1] - 1) // nums[i+1]
            res += needed_splits - 1
            nums[i] = nums[i] // needed_splits
        return res