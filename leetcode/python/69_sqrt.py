class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            m = (l+r) // 2
            if m**2 <= x and (m+1)**2 > x:
                return m
            elif m**2 > x:
                r = m-1
            else:
                l = m+1

s = Solution()
print(s.mySqrt(0))
print(s.mySqrt(1))
print(s.mySqrt(2))
print(s.mySqrt(3))
print(s.mySqrt(4))
print(s.mySqrt(5))
print(s.mySqrt(5))
print(s.mySqrt(7))
print(s.mySqrt(9))
print(s.mySqrt(10))