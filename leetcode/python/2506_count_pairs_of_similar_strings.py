from collections import defaultdict


class Solution:
    def similarPairs(self, words: list[str]) -> int:
        counter = defaultdict(int)
        res: int = 0
        for w in words:
            w = frozenset(w)
            res += counter[w]
            counter[w] += 1
        return res
    
        