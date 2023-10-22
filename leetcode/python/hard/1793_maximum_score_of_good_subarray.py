class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = k
        right = k
        cur = res = nums[k]
    
        while left >= 0 or right < n:
            l_val = nums[left] if left >= 0 else 0
            r_val = nums[right] if right < n else 0
            if l_val > r_val:
                left -= 1
                cur = min(cur, l_val)
            else:
                right += 1
                cur = min(cur, r_val)
            res = max(res, cur * (right - left - 1))
        return res