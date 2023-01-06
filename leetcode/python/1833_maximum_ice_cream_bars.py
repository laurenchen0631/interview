class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        for i, cost in enumerate(costs):
            if cost > coins:
                return i
            coins -= cost
        return len(costs)
                
        