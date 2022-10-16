class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for n in range(num // 2, num + 1):
            if n + int(str(n)[::-1]) == num:
                return True
        return False

s = Solution()
print(s.sumOfNumberAndReverse(443))
print(s.sumOfNumberAndReverse(63))
print(s.sumOfNumberAndReverse(181))
print(s.sumOfNumberAndReverse(0))