class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        res: int = 0
        dp = [0] * (len(nums)+1)
        dpFlip = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            n = nums[i-1]
            if n == 1:
                dp[i] = dp[i-1] + 1
                dpFlip[i] = dpFlip[i-1] + 1
            else:
                dpFlip[i] = dp[i-1] + 1
                dp[i] = 0
            res = max(dpFlip[i], res)
        return res

s = Solution()
print(s.findMaxConsecutiveOnes([1,0,1,1,0]))
print(s.findMaxConsecutiveOnes([1,0,1,1,0,1,1]))
print(s.findMaxConsecutiveOnes([1,1]))
print(s.findMaxConsecutiveOnes([1,0,0]))
print(s.findMaxConsecutiveOnes([0,0,0]))
        