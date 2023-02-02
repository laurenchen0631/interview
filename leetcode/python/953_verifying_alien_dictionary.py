class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        mapping = {c: i for i, c in enumerate(order)}
        for w1, w2 in zip(words, words[1:]):
            if not self.isLess(w1, w2, mapping):
                return False
        return True
    
    def isLess(self, w1: str, w2: str, order: dict[str, int]):
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                return order[c1] < order[c2]
        return len(w1) <= len(w2)
        