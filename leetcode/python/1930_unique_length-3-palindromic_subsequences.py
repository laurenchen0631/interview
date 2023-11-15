import collections


class Solution:
    # aaaaaaa -> 1
    def countPalindromicSubsequence(self, s: str) -> int:
        chars = collections.defaultdict(list[int])
        for i, c in enumerate(s):
            chars[c].append(i)

        res = 0
        for _, locations in chars.items():
            if len(locations) < 2:
                continue
            i, j = locations[0], locations[-1]
            res += len(set(s[i+1:j]))
        return res

        