class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        values = sorted([(n, c) for n, c in zip(nums, cost)])
        n = len(values)
        
        prefix = [0] * n
        prefix[0] = values[0][1]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + values[i][1]
            
        curSum = 0
        for i in range(1, n):
            curSum += values[i][1] * (values[i][0] - values[0][0])
        res = curSum
        
        for i in range(1, n):
            gap = values[i][0] - values[i-1][0]
            curSum += gap * prefix[i-1] 
            curSum -= gap * (prefix[n-1] - prefix[i-1])
            res = min(res, curSum)
        return res