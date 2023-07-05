class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        res = 0
        prev = -1
        consecutive = 0
        for n in nums:
            if n == 1:
                consecutive += 1
            else:
                res = max(res, prev + consecutive)
                prev, consecutive = consecutive, 0
        
        return max(res, prev + consecutive)
    