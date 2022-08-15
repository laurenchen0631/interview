class Solution:
    def __init__(self) -> None:
        self._romanNums = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
            'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
            'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
            'M': 1000, '': 0,
        }

    def romanToInt(self, s: str) -> int:
        res: int = 0
        prev = ''
        for c in s:
            if prev and (k := prev + c) in self._romanNums:
                res += self._romanNums[k]
                prev = ''
            else:
                res += self._romanNums[prev]
                prev = c
        return res + self._romanNums[prev]
    
s = Solution()
print(s.romanToInt('MCMXCIV'))
print(s.romanToInt('LVIII'))
print(s.romanToInt('LIV'))