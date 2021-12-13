from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charPos = dict[str, int]()
        left: int = 0
        right: int = 0
        length: int = 0

        while right < len(s):
            c = s[right]

            index = charPos.get(c)
            if index != None and index >= left:
                left = index + 1
            
            length = max(length, right - left + 1)
            charPos[c] = right
            right += 1
        
        return length

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(""))