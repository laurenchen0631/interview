from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        length: int = 0
        counter = Counter(s)
        hasCenter = False
        for c in counter.keys():
            
            if counter[c] & 1 == 0:
                print(c, counter[c])
                length += counter[c]
            else:
                length += counter[c] - 1
                hasCenter = True
        return length + (1 if hasCenter else 0)

s = Solution()
# print(s.longestPalindrome("abccccdd"))
# print(s.longestPalindrome("a"))
print(s.longestPalindrome("bb"))
