from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: list[list[int]]) -> int:
        incoming = defaultdict(int)
        for u, v, amount in transactions:
            incoming[u] -= amount
            incoming[v] += amount
        
        debts = [amount for amount in incoming.values() if amount != 0]
        n = len(debts)
        
        dp = [-1] * (1 << n)
        dp[0] = 0
        
        def dfs(mask: int) -> int:
            if dp[mask] != -1:
                return dp[mask]
            
            balance, res = 0, 0
            for i in range(n):
                flag = 1 << i
                if mask & flag:
                    balance += debts[i]
                    res = max(res, dfs(mask ^ flag))
                    
            dp[mask] = res + (balance == 0)
            print(dp[mask], bin(mask), balance)
            return dp[mask]

        return n - dfs((1 << n) - 1)