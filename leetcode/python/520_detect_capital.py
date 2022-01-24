import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True
        if word[0].isupper() and word[1].isupper():
            return self.isAllUppercase(word[2:])
        if word[1].islower():
            return self.isAllLowercase(word[2:])
        return False
    
    def isAllUppercase(self, s: str) -> str:
        for c in s:
            if c.islower():
                return False
        return True

    def isAllLowercase(self, s: str) -> str:
        for c in s:
            if c.isupper():
                return False
        return True

    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)

s = Solution()
print(s.detectCapitalUse('USA'))
print(s.detectCapitalUse('FlaG'))
print(s.detectCapitalUse('leetcode'))
print(s.detectCapitalUse('Google'))