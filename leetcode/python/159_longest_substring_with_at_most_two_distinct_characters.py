class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        prev: int | None = None
        cur = curLen = res = 0
        for i in range(len(s)):
            if s[i] == s[cur]:
                curLen += 1
            elif prev is None or s[i] == s[prev]:
                prev, cur = cur, i
                curLen += 1
            else:
                prev, cur = cur, i
                curLen = i - prev + 1
            res = max(res, curLen)
        return res

s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct(s = "eceba"))
print(s.lengthOfLongestSubstringTwoDistinct(s = "ccaabbb"))
print(s.lengthOfLongestSubstringTwoDistinct(s = "abbaacccca"))