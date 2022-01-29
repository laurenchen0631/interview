class Solution:
    def nthUglyNumber(self, n: int) -> int:
        index2: int = 0
        index3: int = 0
        index5: int = 0
        dp = [1] * n
        for i in range(1, n):
            dp[i] = min(dp[index2] * 2, dp[index3] * 3, dp[index5] * 5)

            if dp[i] == dp[index2] * 2:
                index2 += 1
            if dp[i] == dp[index3] * 3:
                index3 += 1
            if dp[i] == dp[index5] * 5:
                index5 += 1
        return dp[-1]

s = Solution()
print(s.nthUglyNumber(1))
print(s.nthUglyNumber(2))
print(s.nthUglyNumber(3))
print(s.nthUglyNumber(4))
print(s.nthUglyNumber(5))
print(s.nthUglyNumber(6))
print(s.nthUglyNumber(7))
print(s.nthUglyNumber(8))
print(s.nthUglyNumber(9))
print(s.nthUglyNumber(10))
print(s.nthUglyNumber(11))
print(s.nthUglyNumber(12))
print(s.nthUglyNumber(13))
print(s.nthUglyNumber(14))
print(s.nthUglyNumber(15))
print(s.nthUglyNumber(16))
print(s.nthUglyNumber(17))
print(s.nthUglyNumber(18))
print(s.nthUglyNumber(19))
print(s.nthUglyNumber(20))
