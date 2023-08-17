

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        firstTransactionCost = prices[0]
        firstTransactionProfit = 0

        mostMoneyInPocket = -prices[0] 
        profitFromTwoTransactions = 0 

        for price in prices:
            firstTransactionCost = min(firstTransactionCost, price) 
            firstTransactionProfit = max(firstTransactionProfit, price-firstTransactionCost)

            mostMoneyInPocket = max(mostMoneyInPocket, firstTransactionProfit-price)
            profitFromTwoTransactions = max(profitFromTwoTransactions, mostMoneyInPocket+price)
        return profitFromTwoTransactions