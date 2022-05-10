class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res: list[list[int]] = []
        self.helper(n, k, [], 1, res)
        return res
    
    def helper(self, n: int, k: int, comb: list[int], start: int, res: list[list[int]]) -> bool:
        if k == 1:
            if n >= start and n < 10:
                res.append(comb + [n])
            return
        
        for i in range(start, 11-k):
            if (19-k) * k // 2 < n - i:
                continue
            comb.append(i)
            self.helper(n-i, k-1, comb, i+1, res)
            comb.pop()
        
s = Solution()
print(s.combinationSum3(k = 3, n = 7))
print(s.combinationSum3(k = 3, n = 9))
print(s.combinationSum3(k = 4, n = 1))
print(s.combinationSum3(k = 2, n = 18))