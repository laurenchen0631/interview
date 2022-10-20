

class Solution:
    def __init__(self) -> None:
        self._roman = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
    def intToRoman(self, num: int) -> str:
        res: list[str] = []
        while num:
            for n, r in self._roman:
                if num >= n:
                    res.append(r)
                    num -= n
                    break
        return ''.join(res)