from collections import Counter

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count = Counter(s)
        frequency = [count[c] for c in count]
        frequency.sort(reverse=True)
        res = 0
        for i, freq in enumerate(frequency):
            pos = 1 + i // 9
            res += pos * freq
        return res