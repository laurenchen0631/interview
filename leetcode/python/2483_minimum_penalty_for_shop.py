class Solution:
    # "YYNY"
    # 00011
    # 32110
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix = [0] * (n + 1)
        postfix = [0] * (n + 1)
        
        for i, c in enumerate(customers):
            prefix[i+1] = prefix[i] + (1 if c == 'N' else 0)
            postfix[n-i-1] = postfix[n-i] + (1 if customers[n-i-1] == 'Y' else 0)
            
        cur_min = prefix[0] + postfix[0]
        res = 0
        for i in range(1, n+1):
            if prefix[i] + postfix[i] < cur_min:
                cur_min = prefix[i] + postfix[i]
                res = i
        return res
            