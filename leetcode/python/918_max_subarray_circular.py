class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total = sum(nums)
        if len(nums) <= 1:
            return total
        negateNums = [-n for n in nums]
        return max(
            self.maxSubArray(nums),
            total + self.maxSubArray(negateNums[1:]),
            total + self.maxSubArray(negateNums[:-1])
        )

    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) < 1:
            return 0
        
        res = curMax = nums[0]
        for n in nums[1:]:
            curMax = max(curMax + n, n)
            res = max(res, curMax)
        return res

s = Solution()
print(s.maxSubarraySumCircular([1,-2,3,-2]))
print(s.maxSubarraySumCircular([5,-3,5]))
print(s.maxSubarraySumCircular([-3,-2,-3]))