from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        count = Counter(nums)
        prev = -1
        skip = using = 0
        for n in sorted(count):
            if prev != n - 1:
                skip, using = max(skip, using), n * count[n] + max(skip, using)
            else:
                skip, using = max(skip, using), n * count[n] + skip
            prev = n
        return max(skip, using)

s = Solution()
print(s.deleteAndEarn([3,4,2]))
print(s.deleteAndEarn([2,2,3,3,3,4]))
