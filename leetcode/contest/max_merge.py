class Solution:
    def maxArrayValue(self, nums: list[int]) -> int:
        cur = 0
        res = 0
        for n in nums[::-1]:
            if n <= cur:
                cur += n
            else:
                cur = n
            res = max(res, cur)
        return res
        

s = Solution()
print(s.maxArrayValue([2,4,3,5,1]))
print(s.maxArrayValue([2,3,7,9,3]))
print(s.maxArrayValue([5,3,3]))
print(s.maxArrayValue([1]))
print(s.maxArrayValue([40,15,35,98,77,79,24,62,53,84,97,16,30,22,49]))
            
        