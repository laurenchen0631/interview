from operator import length_hint
from numpy import char


class Solution:
    def maxProduct(self, words: list[str]) -> int:
        res: int = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                w1 = words[i]
                w2 = words[j]
                letters = set(w1)
                if len(letters.difference(w2)) == len(letters):
                    res = max(res, len(w1) * len(w2))
        return res

s = Solution()
print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(s.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
print(s.maxProduct(["a","aa","aaa","aaaa"]))
print(s.maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]))