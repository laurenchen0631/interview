class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        if len(nums) < k:
            return 0
        
        counter = {}
        duplicates = 0
        cur_sum = 0
        res = 0
        for i, n in enumerate(nums):
            if i >= k:
                l = nums[i-k]
                counter[l] -= 1
                cur_sum -= l
                if counter[l] == 1:
                    duplicates -= 1
            
            counter[n] = counter.get(n, 0) + 1
            cur_sum += n
            if counter[n] == 2:
                duplicates += 1
            
            if i >= k - 1 and duplicates == 0:
                res = max(res, cur_sum)
        return res