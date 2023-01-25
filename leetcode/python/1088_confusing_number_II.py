class Solution:
    def confusingNumberII(self, n: int) -> int:
        digits = [(0, 0), (1, 1), (6, 9), (8, 8), (9, 6)]
        res = 0
        def dfs(num: int, rotated: int, unit: int) -> None:
            if num > n:
                return
            nonlocal res
            if num != rotated:
                res += 1
            for d, r in digits:
                if num == 0 and d == 0:
                    continue
                dfs(num * 10 + d, r * unit + rotated, unit * 10)
        dfs(0, 0, 1)
        return res
    
s = Solution()
print(s.confusingNumberII(20))
print(s.confusingNumberII(1000000000))