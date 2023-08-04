class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1
        while r >= 0:
            if s[r] == " ":
                r -= 1
                continue
            
            l = r
            while l >= 0 and s[l] != " ":
                l -= 1
            return r - l
        return 0
