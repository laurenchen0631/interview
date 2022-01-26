class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) < 1:
            return 0
        
        res = curMax = nums[0]
        for n in nums[1:]:
            curMax = max(curMax + n, n)
            res = max(res, curMax)
        return res
    
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5,4,-1,7,8]))