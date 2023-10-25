class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        res = 0
        for i in range(2, n + 1):
            d, k = divmod(k, 2 ** (n - i))
            if res == 0 and d == 1:
                res = 1
            elif res == 1 and d == 1:
                res = 0
        return res
            