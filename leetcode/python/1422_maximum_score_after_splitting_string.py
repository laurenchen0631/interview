class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = s.count('1')
        res = 0
        for c in s[:-1]:
            if c == '0':
                left += 1
            else:
                right -= 1
            res = max(res, left + right)
        return res