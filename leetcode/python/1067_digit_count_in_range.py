class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        return self.count(d, high) - self.count(d, low-1)

    def count(self, d: int, limit: int):
        count: int = 0
        i: int = 1
        while i <= limit:
            (t, r) = divmod(limit, i) 
            count += ((t + 9 - d) // 10) * i
            count += (r + 1 if t % 10 == d else 0)
            if d == 0:
                count -= i
            i *= 10
        return count

s = Solution()
print(s.digitsCount(d = 3, low = 100, high = 250))