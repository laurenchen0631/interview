class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count: int = 0
        while target > startValue:
            count += 1
            if target & 1 == 1:
                target += 1
            else:
                target //= 2
        return count + (startValue - target)

s = Solution()
print(s.brokenCalc(startValue = 2, target = 3))
print(s.brokenCalc(startValue = 5, target = 8))
print(s.brokenCalc(startValue = 3, target = 10))