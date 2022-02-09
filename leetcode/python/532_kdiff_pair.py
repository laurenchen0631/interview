import collections


class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        pairs: int = 0
        u = collections.Counter(nums)
        for n in u:
            u[n] -= 1
            if n+k in u and u[n+k] > 0:
                pairs += 1
            u[n] += 1
            
        return pairs

s = Solution()
print(s.findPairs(nums = [3,1,4,1,5], k = 2))
print(s.findPairs(nums = [1,2,3,4,5], k = 1))
print(s.findPairs(nums = [1,3,1,5,4], k = 0))