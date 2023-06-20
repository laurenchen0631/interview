class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        res = [-1] * n
        if n < 2 * k + 1:
            return res

        curSum = sum(nums[:2*k+1])
        for i in range(k, n-k):
            res[i] = curSum // (2*k+1)
            curSum = curSum - nums[i-k] + nums[min(i+k+1, n-1)]
        return res