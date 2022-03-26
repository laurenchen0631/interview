from numpy import einsum_path


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {n: i for i, n in enumerate(nums)}
        for i in range(len(nums)-1):
            supplement = target - nums[i]
            if supplement in map and map[supplement] != i:
                return [i, map[supplement]]
        return [0, 1]

s = Solution()
print(s.twoSum(nums = [2,7,11,15], target = 9))
print(s.twoSum(nums = [3,2,4], target = 6))
print(s.twoSum(nums = [3,3], target = 6))