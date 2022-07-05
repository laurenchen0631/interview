class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        res: int = 0
        num = set(nums)
        for n in num:
            if n - 1 in num:
                continue
            
            k = 1
            while n + 1 in num:
                k += 1
                n += 1
            res = max(res, k)
        return res

s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))