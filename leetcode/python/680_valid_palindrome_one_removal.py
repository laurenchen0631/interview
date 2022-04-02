class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.isValid(s[l+1:r+1]) or self.isValid(s[l:r])
        return True

    def isValid(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True


s = Solution()
print(s.validPalindrome('aba'))
print(s.validPalindrome('abc'))
print(s.validPalindrome('abca'))
print(s.validPalindrome('aaaca'))
print(s.validPalindrome("ebcbbececabbacecbbcbe"))