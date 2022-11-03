class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        base = 10
        res = 0
        while self.getDigitSum(n) > target:
            rem = n % base
            res += (base - rem)
            n += (base - rem)
            base *= 10
        return res

    def getDigitSum(self, n: int) -> int:
        return sum([int(digit) for digit in str(n)])

s = Solution()
print(s.makeIntegerBeautiful(n = 16, target = 6))
print(s.makeIntegerBeautiful(n = 467, target = 6))
print(s.makeIntegerBeautiful(n = 1, target = 1))