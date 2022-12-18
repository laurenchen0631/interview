from collections import defaultdict
from math import gcd, sqrt

class Solution:
    def smallestValue(self, n: int) -> int:
        while (factors := self.getPrimeFactors(n)) and len(factors) > 1:
            v = sum(factors)
            if v == n:
                break
            n = v
        return n
    
    def getPrimeFactors(self, n: int) -> list[int]:
        res = []
        for i in range(2, int(sqrt(n)) + 1):
            while n % i == 0:
                res.append(i)
                n //= i
        if n > 1:
            res.append(n)
        return res
    
s = Solution()
print(s.smallestValue(4))