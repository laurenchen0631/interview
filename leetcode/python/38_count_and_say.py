from functools import cache
from operator import le


class Solution:
    def __init__(self):
        self.cache = ['', '1']

    def countAndSay(self, n: int) -> str:
        if len(self.cache) > n:
            return self.cache[n]
        
        for i in range(len(self.cache), n+1):
            s = self.cache[i-1]
            j = 0
            parts: list[str] = []
            while j < len(s):
                count = 0
                c = s[j]
                while j < len(s) and s[j] == c:
                    count += 1
                    j += 1
                parts.append(f'{count}{c}')
            self.cache.append(''.join(parts))
        return self.cache[n]

s = Solution()
print(s.countAndSay(1))
# print(s.countAndSay(2))
# print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(5))