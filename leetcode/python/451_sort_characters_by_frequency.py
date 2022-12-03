from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        return ''.join(sorted(s, key=lambda x: (freq[x], -ord(x)), reverse=True))
    
s = Solution()
print(s.frequencySort("acacac"))
print(s.frequencySort("apple"))