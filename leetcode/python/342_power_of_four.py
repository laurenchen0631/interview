class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n & 0x55555555 > 0

s = Solution()
print(s.isPowerOfFour(16))
print(s.isPowerOfFour(1))
print(s.isPowerOfFour(5))
print(s.isPowerOfFour(8))
print(s.isPowerOfFour(15))