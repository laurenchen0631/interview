class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        index = {words[i]: i for i in range(len(words))}
        res: list[list[int]] = []
        for w in words:
            for i in range(len(w)+1):
                pre = w[:i]
                suf = w[i:]
                if self.isPalindrome(pre) and (front := suf[::-1]) in index and front != w:
                    res.append([index[front], index[w]])
                if self.isPalindrome(suf) and i != len(w) and (back := pre[::-1]) in index and back != w:
                    res.append([index[w], index[back]])
        return res

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

s = Solution()
print(s.palindromePairs(["abcd","dcba","lls","s","sssll"]))
print(s.palindromePairs(["a",""]))