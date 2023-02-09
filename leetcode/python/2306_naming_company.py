class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        groups = [set[str]() for i in range(26)]
        for word in ideas:
            groups[ord(word[0]) - ord('a')].add(word[1:])
        res = 0
        for i in range(25):
            for j in range(i+1, 26):
                conflict = groups[i] & groups[j]
                res += 2 * (len(groups[i]) - len(conflict)) * (len(groups[j]) - len(conflict))
        return res