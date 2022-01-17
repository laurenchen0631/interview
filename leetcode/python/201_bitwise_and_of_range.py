class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift: int = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

s = Solution()
print(s.rangeBitwiseAnd(5,7))
print(s.rangeBitwiseAnd(0,0))
print(s.rangeBitwiseAnd(1,21421312))