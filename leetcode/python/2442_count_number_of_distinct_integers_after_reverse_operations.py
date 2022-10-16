class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        numsSet = set(nums)
        for n in nums:
            s = str(n)
            if s != s[::-1]:
                numsSet.add(int(s[::-1]))
        return len(numsSet)

s = Solution()
print(s.countDistinctIntegers([1,13,10,12,31]))
print(s.countDistinctIntegers([2,2,2]))