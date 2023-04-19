class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        res = []
        for c1, c2 in zip(word1, word2):
            res.append(c1)
            res.append(c2)
        return ''.join(res) + word1[n:] + word2[n:]