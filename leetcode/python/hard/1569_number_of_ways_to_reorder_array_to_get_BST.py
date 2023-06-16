from math import comb


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        def dfs(nums: list[int]) -> int:
            n = len(nums)
            if n <= 2:
                return 1
            left = [x for x in nums if x < nums[0]]
            right = [x for x in nums if x > nums[0]]
            return comb(n - 1, len(left)) * dfs(left) * dfs(right) % MOD
        return dfs(nums) - 1