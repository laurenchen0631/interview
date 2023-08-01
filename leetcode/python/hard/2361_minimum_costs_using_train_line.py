class Solution:
    def minimumCosts(self, regular: list[int], express: list[int], expressCost: int) -> list[int]:
        n = len(regular)
        dp_reg = [0] * (n + 1)
        dp_exp = [0] * (n + 1)
        res = []
        
        for i in range(1, n+1):
            dp_reg[i] = min(dp_reg[i-1] + regular[i-1], dp_exp[i-1] + regular[i-1])
            dp_exp[i] = min(dp_exp[i-1] + express[i-1], dp_reg[i-1] + expressCost + express[i-1])
            res.append(min(dp_reg[i], dp_exp[i]))
        return res