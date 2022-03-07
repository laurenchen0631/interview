class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        MOD = 10**9 + 7
        for i in range(1, 2*n + 1):
            if i & 1 == 0:
                res *= (i >> 1)
            else:
                res *= i
            res %= MOD
        return res

s = Solution()
print(s.countOrders(2))
print(s.countOrders(3))
print(s.countOrders(4))
print(s.countOrders(5))