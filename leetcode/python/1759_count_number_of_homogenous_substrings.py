class Solution:
    def countHomogenous(self, s: str) -> int:
        consecutive = 1
        prev = ""
        res = 0
        for c in s:
            if c == prev:
                consecutive += 1
            else:
                consecutive = 1
            res = (res + consecutive) % (10 ** 9 + 7)
            prev = c
        return res
        
        