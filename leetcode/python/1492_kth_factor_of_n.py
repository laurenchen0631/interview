from math import sqrt


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for x in range(1, int(sqrt(n)) + 1):
            if n % x == 0:
                k -= 1
                if k == 0:
                    return x
                else:
                    factors.append(x)
        if factors[-1] * factors[-1] == n:
            k += 1

        f = len(factors)
        return n // factors[f - k] if k <= f else -1