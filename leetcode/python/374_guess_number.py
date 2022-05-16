def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            m = (l + r) // 2
            if guess(m) == 0:
                return m
            elif guess(m) == 1:
                l = m + 1
            else:
                r = m - 1
        return 0