class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        base = ord('a') - 1
        res: list[str] = []
        for i in range(n-1, -1, -1):
            v = min(26, k-i)
            res.append(chr(base + v))
            k -= v
        return ''.join(reversed(res))

s = Solution()
print(s.getSmallestString(n = 3, k = 27))
print(s.getSmallestString(n = 5, k = 73))