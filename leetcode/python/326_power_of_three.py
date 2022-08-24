
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return 3 ** 19 % n == 0 if n > 0 else False

s = Solution()
print(s.isPowerOfThree(27))
print(s.isPowerOfThree(243))