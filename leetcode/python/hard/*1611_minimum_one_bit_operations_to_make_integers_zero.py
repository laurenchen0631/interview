import math

class Solution:
    # 110 -> 010 -> 011 -> 001 -> 000
    # [1000] -> 1001 -> 1011 -> 1010 -> [1100] -> [0100]
    # greedy: start from leftmost bit?
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        k = math.floor(math.log2(n))
        return 2 ** (k+1) - 1 - self.minimumOneBitOperations(n ^ (2 ** k))
        