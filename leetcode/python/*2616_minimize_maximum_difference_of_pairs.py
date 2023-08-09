class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        
        def countPairs(threshold: int) -> int:
            cnt = 0
            i = 0
            while i < n - 1:
                if nums[i+1] - nums[i] <= threshold:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt
        
        l = 0
        r = nums[-1] - nums[0]
        while l < r:
            m = (l + r) // 2
            if countPairs(m) >= p:
                r = m
            else:
                l = m + 1
        return l