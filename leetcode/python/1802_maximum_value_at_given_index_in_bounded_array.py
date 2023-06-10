class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l, r = 1, maxSum
        while l < r:
            m = (l + r + 1) // 2
            if self.getSum(n, index, m) <= maxSum:
                # use (l+r+1)//2 to avoid infinite loop
                l = m
            else:
                r = m - 1
        return l
    
    def getSum(self, n: int, index: int, m: int) -> int:
        l = max(m - index, 1)
        lSum = (l + m) * (m - l + 1) // 2 + max(0, index - m + 1)
        r = max(m - (n - index - 1), 1)
        rSum = (r + m) * (m - r + 1) // 2 + max(0, n - index - m)
        return lSum + rSum - m