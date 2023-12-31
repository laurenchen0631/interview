
from collections import defaultdict


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pos = defaultdict(list[int])
        for i, c in enumerate(s):
            pos[c].append(i)
        
        res = -1
        for c, indices in pos.items():
            if len(indices) > 1:
                res = max(res, indices[-1] - indices[0] - 1)
        return res