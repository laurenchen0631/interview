from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        remaining = len(t)
        curL = l = 0
        minLen = len(s) + 1
        for r in range(len(s)):
            if counter[s[r]] > 0:
                remaining -= 1
            counter[s[r]] -= 1
            while remaining == 0:
                if r - curL + 1 < minLen:
                    minLen = r - curL + 1
                    l = curL
                counter[s[curL]] += 1
                if counter[s[curL]] > 0:
                    remaining += 1
                curL += 1
        return s[l:l + minLen] if minLen <= len(s) else ""


s = Solution()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))