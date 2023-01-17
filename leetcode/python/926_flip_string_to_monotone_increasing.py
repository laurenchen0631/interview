from collections import Counter


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        right = Counter(s)
        left = {'0': 0, '1': 0}
        flips = right['0']
        for b in s:
            left[b] += 1
            right[b] -= 1
            flips = min(flips, left['1'] + right['0'])
        return flips
        