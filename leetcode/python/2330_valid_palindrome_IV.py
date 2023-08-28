class Solution:
    # 5: 0, 1, 2, 3, 4
    # 6: 0, 1, 2, 3, 4, 5
    def makePalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        diff = 0
        while l < r:
            if s[l] != s[r]:
                diff += 1
            if diff > 2:
                return False
            l += 1
            r -= 1
        return True