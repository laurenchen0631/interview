class Solution:
    def minSteps(self, n: int) -> int:
        res: int = 0
        factor: int = 2
        while n > 1:
            while n % factor == 0:
                res += factor
                n //= factor
            factor += 1
        return res

s = Solution()
print(s.minSteps(3))
print(s.minSteps(4))
print(s.minSteps(5))
print(s.minSteps(6))
print(s.minSteps(15))