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
    
    def minDeletionsOpt(self, s: str) -> int:
        count = Counter(s)
        freq = sorted(count.values(), reverse=True)
        res = 0
        # 3 2 1 1 1
        for i in range(1, len(freq)):
            if freq[i] >= freq[i-1]:
                res += freq[i] - freq[i-1] + 1
                freq[i] = freq[i-1] - 1
                if freq[i] < 0:
                    freq[i] = 0
                    res -= 1
        return res

s = Solution()
print(s.minDeletions(s = "aab"))
print(s.minDeletions(s = "aaabbbcc"))
print(s.minDeletions(s = "ceabaacb"))
print(s.minDeletionsOpt(s = "abc"))


