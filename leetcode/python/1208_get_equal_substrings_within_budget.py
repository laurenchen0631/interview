class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        start = 0
        end = 0
        sum_cost = 0
        max_len = 0
        while end < n:
            sum_cost += cost[end]
            while sum_cost > maxCost:
                sum_cost -= cost[start]
                start += 1
            max_len = max(max_len, end - start + 1)
            end += 1
        return max_len
