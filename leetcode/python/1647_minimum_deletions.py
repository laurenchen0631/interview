from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        unique = set[int]()
        deletions: int = 0
        for c in freq.keys():
            while freq[c] in unique and freq[c] > 0:
                freq[c] -= 1
                deletions += 1
            unique.add(freq[c])
        return deletions

s = Solution()
print(s.minDeletions(s = "aab"))
print(s.minDeletions(s = "aaabbbcc"))
print(s.minDeletions(s = "ceabaacb"))


