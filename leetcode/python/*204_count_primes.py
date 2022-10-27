from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        """Sieve of Eratosthenes"""
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(sqrt(n)) + 1):
            if primes[i]:
                for k in range(i * i, n, i):
                    primes[k] = False
        return sum(primes)

s = Solution()
print(s.countPrimes(10))