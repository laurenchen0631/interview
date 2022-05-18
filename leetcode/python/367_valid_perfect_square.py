class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while l <= r:
            m = (l+r) // 2
            if m * m == num:
                return True
            elif m*m > num:
                r = m - 1
            else:
                l = m + 1
        return False

s = Solution()
print(s.isPerfectSquare(0))
print(s.isPerfectSquare(1))
print(s.isPerfectSquare(2))
print(s.isPerfectSquare(3))
print(s.isPerfectSquare(4))
print(s.isPerfectSquare(5))
print(s.isPerfectSquare(6))