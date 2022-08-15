from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counter = defaultdict(int)
        a, b = 0, 0
        for i in range(len(secret)):
            c1, c2 = secret[i], guess[i]
            if c1 == c2:
                a += 1
                continue
            
            counter[c1] += 1
            if counter[c1] <= 0:
                b += 1
            counter[c2] -= 1
            if counter[c2] >= 0:
                b += 1
        return f"{a}A{b}B"

s = Solution()
print(s.getHint(secret = "1807", guess = "7810"))
print(s.getHint(secret = "1123", guess = "0111"))