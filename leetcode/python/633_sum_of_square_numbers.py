import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(0, math.floor(math.sqrt(c))+1):
            b = c - a * a
            if self.isSquare(b):
                return True
        return False
    
    def isSquare(self, n: int) -> int:
        return math.sqrt(n) % 1 == 0


s = Solution()
print(s.judgeSquareSum(1))
print(s.judgeSquareSum(2))
print(s.judgeSquareSum(3))
print(s.judgeSquareSum(4))
print(s.judgeSquareSum(5))
print(s.judgeSquareSum(6))
print(s.judgeSquareSum(7))
print(s.judgeSquareSum(8))
print(s.judgeSquareSum(9))
print(s.judgeSquareSum(10))