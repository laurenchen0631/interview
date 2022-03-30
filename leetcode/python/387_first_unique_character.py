from typing import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1

s = Solution()
print(s.firstUniqChar(s = "leetcode"))
print(s.firstUniqChar(s = "loveleetcode"))
print(s.firstUniqChar(s = "aabb"))