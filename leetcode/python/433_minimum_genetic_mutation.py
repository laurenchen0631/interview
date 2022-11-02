class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        unused = set(bank)
        q = [start]
        res = 0
        while q:
            tmp = []
            for g1 in q:
                if g1 == end:
                    return res
                for g2 in list(unused):
                    if self.isOneDiff(g1, g2):
                        tmp.append(g2)
                        unused.remove(g2)
            q = tmp
            res += 1
        return -1

    def isOneDiff(self, s1: str, s2: str) -> bool:
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

s = Solution()
print(s.minMutation(start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]))
print(s.minMutation(start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))
print(s.minMutation(start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]))