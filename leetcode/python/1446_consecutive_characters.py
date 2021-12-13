class Solution:
    def maxPower(self, s: str) -> int:
        power: int = 0
        prevChar: str = ''
        count: int = 0
        for c in s:
            if c != prevChar:
                prevChar = c
                power = max(power, count)
                count = 1
            else:
                count += 1
        return max(power, count)