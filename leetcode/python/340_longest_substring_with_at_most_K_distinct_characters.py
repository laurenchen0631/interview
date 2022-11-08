from collections import OrderedDict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = res = 0
        chars = OrderedDict()
        for r, c in enumerate(s):
            if c in chars:
                del chars[c]
            chars[c] = r
            if len(chars) > k:
                _, l = chars.popitem(last=False)
                l += 1
            res = max(res, r - l + 1)
        return res