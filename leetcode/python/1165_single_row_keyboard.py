class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        prev = keyboard[0]
        res = 0
        chars = {keyboard[i]: i for i in range(26)}
        for c in word:
            res += abs(chars[c] - chars[prev])
            prev = c
        return res