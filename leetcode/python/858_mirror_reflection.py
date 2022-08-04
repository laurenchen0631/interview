class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0: p, q = p / 2, q / 2
        print(p, q)
        print(p % 2, q % 2)
        return int(1 - p % 2 + q % 2)

s = Solution()
# print(s.mirrorReflection(2, 1))
# print(s.mirrorReflection(3, 1))
print(s.mirrorReflection(3, 2))