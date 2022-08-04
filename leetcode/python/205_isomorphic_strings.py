class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        replaceS = dict[str, str]()
        replaceT = dict[str, str]()
        for i in range(len(s)):
            if s[i] not in replaceS and t[i] not in replaceT:
                replaceS[s[i]] = t[i]
                replaceT[t[i]] = s[i]
            elif replaceS.get(s[i]) != t[i] or replaceT.get(t[i]) != s[i]:
                return False
        return True

s = Solution()
print(s.isIsomorphic(s = "egg", t = "add"))
print(s.isIsomorphic(s = "foo", t = "bar"))
print(s.isIsomorphic(s = "paper", t = "title"))
print(s.isIsomorphic(s = "badc", t = "baba"))