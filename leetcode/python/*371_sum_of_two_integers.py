class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        if x < y:
            x, y = y, x
            a, b = b, a
        sign = 1 if a > 0 else -1
        if a * b >= 0:
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        return x * sign

s = Solution()
print(s.getSum(3,4))
print(s.getSum(3,-1))
print(s.getSum(0, 17))
print(s.getSum(-1,-4))