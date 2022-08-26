from collections import Counter
import math

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n1 = str(n)
        base = 2 ** math.ceil(math.log2(10 ** (len(n1) - 1)))
        nc = Counter(n1)
        for k in [1, 2, 4, 8]:
            n2 = str(base * k)
            if len(n2) > len(n1):
                break
            if nc == Counter(n2):
                return True
        return False

s = Solution()
print(s.reorderedPowerOf2(61))
print(s.reorderedPowerOf2(23))
print(s.reorderedPowerOf2(232))
print(s.reorderedPowerOf2(4012))