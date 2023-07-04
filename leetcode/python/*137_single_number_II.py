class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                cnt += (num >> i) & 1
            res |= (cnt % 3) << i
        
        if res >= (1 << 31):
            res -= (1 << 32)
        return res