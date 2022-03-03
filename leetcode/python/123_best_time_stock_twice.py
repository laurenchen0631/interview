from turtle import right


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
            
        leftDP = [0] * n
        leftMin = prices[0]

        rightDP = [0] * (n + 1)
        rightMax = prices[-1]
        
        for i in range(1, len(prices)):
            leftMin = min(leftMin, prices[i])
            leftDP[i] = max(leftDP[i-1], prices[i] - leftMin)
            
            j = n-1-i
            rightMax = max(rightMax, prices[j])
            rightDP[j] = max(rightDP[j+1], rightMax - prices[j])

        maxProfit = 0
        for i in range(n):
            maxProfit = max(maxProfit, leftDP[i] + rightDP[i+1])
        return maxProfit

s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))
print(s.maxProfit([7,1,5,3,6,4]))