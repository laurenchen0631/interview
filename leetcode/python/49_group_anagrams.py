from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list[int])
        for word in strs:
            letters = [0] * 26
            for w in word:
                letters[ord(w) - ord('a')] += 1
            key = tuple(letters)
            anagrams[key].append(word)
        return list(anagrams.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))