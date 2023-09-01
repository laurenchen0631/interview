class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = self.lcs(s, t)
        return len(t) - n

    def lcs(self, s: str, t: str) -> int:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        return j