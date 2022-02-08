class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        m = num % 9
        return m if m != 0 else 9

s = Solution()
print(s.addDigits(0))
print(s.addDigits(38))