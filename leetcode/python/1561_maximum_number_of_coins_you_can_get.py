class Solution:
    # [9,8,7,6,5,1,2,3,4]
    # [1,2,3,4,5,6,7,8,9] -> 8 + 6 + 4

    # [2,4,1,2,7,8]
    # [1,2,2,4,7,8] -> 7 + 2
    def maxCoins(self, piles: list[int]) -> int:
        n = len(piles) // 3
        piles.sort()

        res = 0
        for i in range(n):
            res += piles[-2 - 2 * i]
        return res
        