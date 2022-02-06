class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) < 1:
            return True
        sIndex: int = 0
        for c in t:
            if s[sIndex] == c:
                sIndex += 1
                if sIndex == len(s):
                    return True
        return False

s = Solution()
print(s.isSubsequence(s = "abc", t = "ahbgdc"))
print(s.isSubsequence(s = "axc", t = "ahbgdc"))