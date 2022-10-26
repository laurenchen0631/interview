class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix = {0: 0}
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            r = cur % k
            if r not in prefix:
                prefix[r] = i+1
            elif i - prefix[r] > 0:
                return True
                
        return False

s = Solution()
print(s.checkSubarraySum(nums = [23,2,6,4,7], k = 6))