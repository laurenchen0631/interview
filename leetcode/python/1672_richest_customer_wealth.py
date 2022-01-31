import re


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maximum: int = 0
        for customer in accounts:
            wealth = sum(customer)
            maximum = max(wealth, maximum)
        return maximum
    
s = Solution()
print(s.maximumWealth([[1,2,3],[3,2,1]]))
print(s.maximumWealth([[1,5],[7,3],[3,5]]))
print(s.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))