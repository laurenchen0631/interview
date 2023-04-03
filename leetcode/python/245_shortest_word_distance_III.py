class Solution:
    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        res = len(wordsDict)
        prev = -1
        for i, w in enumerate(wordsDict):
            if w == word1 or w == word2:
                if prev != -1 and (word1 == word2 or wordsDict[prev] != w):
                    res = min(res, i - prev)
                prev = i
        return res