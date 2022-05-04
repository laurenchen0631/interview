
from collections import Counter

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        res: int = 0
        counter = Counter(nums)
        for n in nums:
            if counter[n] == 0:
                continue

            counter[n] -= 1
            if k-n in counter and counter[k-n] > 0:
                res += 1
                counter[k-n] -= 1
        return res

s = Solution()
print(s.maxOperations(nums = [1,2,3,4], k = 5))
print(s.maxOperations(nums = [3,1,3,4,3], k = 6))