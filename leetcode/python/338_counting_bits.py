class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0] * (n+1)
        if n > 1:
            res[1] = 1
        highestBit = 1
        for i in range(1, n+1):
            if i == highestBit << 1:
                highestBit <<= 1
                res[i] = 1
            else:
                res[i] = 1 + res[i - highestBit]
        return res

s = Solution()
print(s.countBits(1))