class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        MAX: int = 123456789
        res: list[int] = []
        for digits in range(len(str(low)), len(str(high)) + 1):
            unit = 10 ** (digits - 1)
            n = MAX // (10 ** (9-digits))
            for j in range(10 - digits):
                if n > high:
                    return res
                if n >= low:
                    res.append(n)
                n = (n%unit)*10 + (digits+1+j)
        return res

s = Solution()
print(s.sequentialDigits(10, 3000))
print(s.sequentialDigits(58, 123))