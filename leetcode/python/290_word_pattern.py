import enum


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternDict = dict[str, str]()
        wordDict = dict[str, str]()
        words = s.split(' ')
        if len(pattern) != len(words) :
            return False
        
        for i, c in enumerate(pattern):
            if c in patternDict:
                if patternDict[c] != words[i]:
                    return False
            if words[i] in wordDict:
                if wordDict[words[i]] != c:
                    return False
            else:
                patternDict[c] = words[i]
                wordDict[words[i]] = c
        return True

s = Solution()
print(s.wordPattern(pattern = "abba", s = "dog cat cat dog"))
print(s.wordPattern("abba", s = "dog cat cat fish"))
print(s.wordPattern("aaaa", s = "dog cat cat dog"))
print(s.wordPattern("abba", "dog dog dog dog"))
