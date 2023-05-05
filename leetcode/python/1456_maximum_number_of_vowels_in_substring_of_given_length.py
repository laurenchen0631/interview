class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        voewls = set(['a', 'e', 'i', 'o', 'u'])
        for c in s[:min(len(s), k)]:
            if c in voewls:
                res += 1
        count = res
        for i in range(k, len(s)):
            if s[i] in voewls:
                count += 1
            if s[i - k] in voewls:
                count -= 1
            res = max(res, count)
        return res