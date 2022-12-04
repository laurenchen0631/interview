class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        n = len(nums)
        r = sum(nums)
        diff = r + 1
        l = 0
        res = -1
        for i in range(n):
            l += nums[i]
            r -= nums[i]
            lAvg = l // (i + 1)
            rAvg = r // (n - i - 1) if i < n - 1 else 0
            
            if (k := abs(lAvg - rAvg)) < diff:
                diff = k
                res = i
        return res
        
s = Solution()
print(s.minimumAverageDifference([2,5,3,9,5,3]))
print(s.minimumAverageDifference([0]))