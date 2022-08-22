# Cycle detection
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {1}
        while n not in visited:
            visited.add(n)
            n = self.getSumOfDigitSquare(n)
            print(n)
        return n == 1
    
    def getSumOfDigitSquare(self, n: int) -> int:
        res: int = 0
        while n > 0:
            n, digit = divmod(n, 10)
            res += digit ** 2
        return res

s = Solution()
print(s.isHappy(19))
# print(s.isHappy(2))
print(s.isHappy(3))
# print(s.isHappy(4))
# print(s.isHappy(5))
# print(s.isHappy(6))