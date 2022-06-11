class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        current = sum(nums)
        n = len(nums)
        res = n+1
        l = 0
        for r in range(n):
            current -= nums[r]
            while current < x and l <= r:
                current += nums[l]
                l += 1
            if current == x:
                res = min(res, l + (n-1-r))
        return res if res < n+1 else -1

s = Solution()
print(s.minOperations(nums = [1,1,4,2,3], x = 5))
print(s.minOperations(nums = [5,6,7,8,9], x = 4))
print(s.minOperations(nums = [3,2,20,1,1,3], x = 10))