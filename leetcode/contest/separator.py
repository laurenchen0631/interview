class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        res = []
        for word in words:
            for w in word.split(separator):
                if w != "":
                    res.append(w)
        return res
    
s = Solution()

print(s.splitWordsBySeparator(words = ["one.two.three","four.five","six"], separator = "."))
print(s.splitWordsBySeparator(words = ["$easy$","$problem$"], separator = "$"))
print(s.splitWordsBySeparator(words = ["|||"], separator = "|"))