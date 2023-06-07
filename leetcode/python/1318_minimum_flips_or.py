class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips: int = 0
        while a > 0 or b > 0 or c > 0:
            d1, d2 = a & 1, b & 1
            target = c & 1
            if (d1, d2, target) == (0, 0, 1):
                flips += 1
            elif target == 0:
                flips += d1 + d2
            a >>= 1
            b >>= 1
            c >>= 1
        return flips