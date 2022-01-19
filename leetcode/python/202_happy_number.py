# Cycle detection
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set[int]([n])
        while n != 1:
            n = self.getSumOfDigitSquare(n)
            if n in visited:
                return False
            visited.add(n)
        return True
    
    def getSumOfDigitSquare(self, n: int) -> int:
        res: int = 0
        while n > 0:
            n, digit = divmod(n, 10)
            res += digit ** 2
        return res

s = Solution()
# print(s.isHappy(19))
# print(s.isHappy(2))
print(s.isHappy(3))
# print(s.isHappy(4))
# print(s.isHappy(5))
# print(s.isHappy(6))