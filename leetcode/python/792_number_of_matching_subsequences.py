class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        res: int = 0
        buckets = [[] for _ in range(26)]
        for i in range(len(words)):
            buckets[ord(words[i][0]) - ord('a')].append((i, 0))
        
        for c in s:
            order = ord(c) - ord('a')
            items = buckets[order]
            buckets[order] = []
            for i, j in items:
                if j + 1 == len(words[i]):
                    res += 1
                else:
                    buckets[ord(words[i][j+1]) - ord('a')].append((i, j+1))
        return res

s = Solution()
print(s.numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))
print(s.numMatchingSubseq(s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))
        