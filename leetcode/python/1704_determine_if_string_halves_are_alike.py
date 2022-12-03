from collections import defaultdict


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        first = 0
        second = 0
        for c in s[:len(s)//2]:
            if c in vowels:
                first += 1
        for c in s[len(s)//2:]:
            if c in vowels:
                second += 1
        return first == second
    
s = Solution()
print(s.halvesAreAlike(("book")))
print(s.halvesAreAlike(("AbCdEfGh")))