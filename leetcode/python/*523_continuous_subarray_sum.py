class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix = {0: -1}
        cur = 0
        for i, n in enumerate(nums):
            cur += n
            rem = cur % k
            if rem not in prefix:
                prefix[rem] = i
            elif i - prefix[rem] > 1:
                return True
                
        return False

s = Solution()
print(s.checkSubarraySum(nums = [23,2,6,4,7], k = 6))
print(s.checkSubarraySum(nums = [13, 12], k = 6))
print(s.checkSubarraySum(nums = [2,4,3], k = 6))