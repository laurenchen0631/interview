import sys

class Solution:
    def maxScore(self, nums: list[int], x: int) -> int:
        n = len(nums)
        dp = [-sys.maxsize] * n
        dp[0] = nums[0]
        cur_max = [nums[0], nums[0]] if nums[0] & 1 == 0 else [nums[0] - x, nums[0]]
        
        for i in range(1, n):
            [even, odd] = cur_max
            new_even, new_odd = even, odd
            parity = nums[i] & 1
            if parity == 1: # odd
                new_odd = max(new_odd, odd + nums[i])
                new_odd = max(new_odd, even + nums[i] - x)
            else: # even
                new_even = max(new_even, even + nums[i])
                new_even = max(new_even, odd + nums[i] - x)
            
            dp[i] = max(new_even, new_odd)
            cur_max = [new_even, new_odd]
        return max(dp)
    
s = Solution()
print(s.maxScore(nums = [2,3,6,1,9,2], x = 5))
print(s.maxScore(nums = [2,4,6,8], x = 3))
print(s.maxScore([9,58,17,54,91,90,32,6,13,67,24,80,8,56,29,66,85,38,45,13,20,73,16,98,28,56,23,2,47,85,11,97,72,2,28,52,33], 90))
        