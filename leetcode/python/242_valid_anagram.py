
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = Counter(t)
        for c in s:
            if c not in counter or counter[c] == 0:
                return False
            counter[c] -= 1
        return True

s = Solution()
print(s.isAnagram('rat', 'tart'))
print(s.isAnagram(s = "anagram", t = "nagaram"))
print(s.isAnagram(s = "rat", t = "car"))