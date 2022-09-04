class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        res: list[int] = []
        def helper(x: int, d: int, n: int) -> None:
            if n == 0:
                res.append(x)
                return
            if d + k < 10:
                helper(10 * x + d + k, d + k, n - 1)
            if d - k >= 0 and k != 0:
                helper(10 * x + d - k, d - k, n - 1)
        for i in range(1, 10):
            helper(i, i, n - 1)
        return res

s = Solution()
print(s.numsSameConsecDiff(n = 3, k = 7))
print(s.numsSameConsecDiff(n = 2, k = 1))