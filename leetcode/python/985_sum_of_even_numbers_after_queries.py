class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        cur = sum([x for x in nums if not x & 1])
        res: list[int] = []
        for v, i in queries:
            n = nums[i]
            nums[i] += v
            if not n & 1 and not nums[i] & 1:
                cur += v
            elif not n & 1 and nums[i] & 1:
                cur -= n
            elif not nums[i] & 1:
                cur += nums[i]
            res.append(cur)
        return res