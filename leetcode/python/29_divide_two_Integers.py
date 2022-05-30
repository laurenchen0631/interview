class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg: int = 0
        if dividend < 0:
            neg += 1
            dividend = -dividend
        if divisor < 0:
            neg += 1
            divisor = -divisor
        
        cache: list[tuple[int, int]] = []
        power = 1
        while dividend >= divisor:
            cache.append((power, divisor))
            power += power
            divisor += divisor
        
        res: int = 0
        for (power, div) in reversed(cache):
            if dividend >= div:
                res += power
                dividend -= div

        res = res if neg != 1 else -res
        if res >= (MAX := 2**31):
            return MAX - 1
        elif res < (MIN := -2**31):
            return MIN 
        return res

s = Solution()
print(s.divide(13, 2))
print(s.divide(-2147483648, 1))