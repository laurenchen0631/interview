import collections


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        sumDict = collections.defaultdict(int)
        sumDict[0] = 1
        subtotal: int = 0
        res: int = 0
        for n in nums:
            subtotal += n
            if subtotal - k in sumDict:
                res += sumDict[subtotal-k]
            sumDict[subtotal] += 1
        return res

s = Solution()
print(s.subarraySum(nums = [1,1,1], k = 2))
print(s.subarraySum(nums = [1,2,3], k = 3))
print(s.subarraySum(nums = [1,3,-1,1,0,3], k = 3))