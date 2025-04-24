from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        group: dict[int, int] = defaultdict(int)
        max_value = 0
        for k in range(1, n + 1):
            c = 0
            while k > 0:
                c += k % 10
                k //= 10
            group[c] += 1
            if group[c] > max_value:
                max_value = group[c]
        return sum(1 for k in group if group[k] == max_value)
