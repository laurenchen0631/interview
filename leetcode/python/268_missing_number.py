class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        bucket = set(range(0, len(nums)+1))
        for n in nums:
            bucket.remove(n)
        return bucket.pop()

s = Solution()
print(s.missingNumber([3,0,1]))
print(s.missingNumber([0,1]))
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))