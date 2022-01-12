class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0

        res: int = 0
        count: int = 2
        diff = nums[1] - nums[0]
        for i in range(1, len(nums)):
            if i < len(nums) - 1 and nums[i] + diff == nums[i+1]:
                count += 1
                continue

            if count >= 3:
                res += ((count-2) * (count-1) // 2)
            if i != len(nums) - 1:
                diff = nums[i+1] - nums[i]
                count = 2
        return res

s = Solution()
print(s.numberOfArithmeticSlices([1,2,3,4]))
print(s.numberOfArithmeticSlices([1,3,5,7,9]))
print(s.numberOfArithmeticSlices([1,3,5,8,11,14,15,16,17]))