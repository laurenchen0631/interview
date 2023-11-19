class Solution:
    # [1,2,2,3,3,5,5] 2 -> 2 + 4 -> 2 + 6
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort()
        prev = nums[-1] + 1
        res = 0
        mini = nums[0]
        for i in range(len(nums)-1, -1, -1):
            if prev != nums[i]:
                res += (len(nums) - i - 1)
                prev = nums[i]
            if nums[i] == mini:
                break
        return res