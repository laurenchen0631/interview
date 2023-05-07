class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        res = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, (r - l))
                l += 1
        return res % (10 ** 9 + 7)