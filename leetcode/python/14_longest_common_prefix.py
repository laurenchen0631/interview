class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s = strs[0]
        for i in range(len(s)):
            for w in strs[1:]:
                if i >= len(w) or w[i] != s[i]:
                    return s[:i]
        return s

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","doggy","doge"]))
        