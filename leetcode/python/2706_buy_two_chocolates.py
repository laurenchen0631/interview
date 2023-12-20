class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        first_min = second_min = 101
        for price in prices:
            if price < first_min:
                second_min = first_min
                first_min = price
            elif price < second_min:
                second_min = price
        
        res = money - first_min - second_min
        return res if res >= 0 else money
        