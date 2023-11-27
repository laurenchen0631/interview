from functools import cache


class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        @cache
        def dp(digit: int, k: int) -> int:
            if k == 0:
                return 1
            if k == 1:
                return len(moves[digit])
            
            res: int = 0
            for next_digit in moves[digit]:
                res = (res + dp(next_digit, k - 1)) % MOD
            return res

        res = 0
        for i in range(0, 10):
            res = (res + dp(i, n-1)) % MOD
        return res
        