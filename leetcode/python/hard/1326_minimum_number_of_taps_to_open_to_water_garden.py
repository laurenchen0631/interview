class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        max_reach = [0] * (n+1)
        for i, r in enumerate(ranges):
            start = max(0, i - r)
            end = min(n, i + r)
            max_reach[start] = max(max_reach[start], end)

        res = cur_end = next_end = 0

        for i in range(n+1):
            if i > next_end:
                return -1
            if i > cur_end:
                res += 1
                cur_end = next_end
            
            next_end = max(next_end, max_reach[i])
        return res