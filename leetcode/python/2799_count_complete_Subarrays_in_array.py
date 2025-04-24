class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        res = 0
        count: dict[int, int] = {}
        n = len(nums)
        r = 0
        distinct = len(set(nums))
        for l in range(n):
            if l > 0:
                count[nums[l - 1]] -= 1
                if count[nums[l - 1]] == 0:
                    count.pop(nums[l - 1])
            while r < n and len(count) < distinct:
                count[nums[r]] = count.get(nums[r], 0) + 1
                r += 1
            if len(count) == distinct:
                res += n - r + 1
        return res
