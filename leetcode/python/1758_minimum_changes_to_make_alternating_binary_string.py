class Solution:
    def minOperations(self, s: str) -> int:
        start0: int = 0
        for i, b in enumerate(s):
            if i % 2 == 0:
                if b != '0':
                    start0 += 1
            else:
                if b != '1':
                    start0 += 1
        return min(start0, len(s) - start0)