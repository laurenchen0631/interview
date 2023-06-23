class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        dp = dict[tuple[int, int], int]()
        for r in range(1, len(nums)):
            for l in range(r):
                diff = nums[l] - nums[r]
                dp[(r, diff)] = dp.get((l, diff), 1) + 1
        return max(dp.values())