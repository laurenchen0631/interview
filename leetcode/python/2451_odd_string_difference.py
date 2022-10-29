class Solution:
    def oddString(self, words: list[str]) -> str:
        words.sort(key=lambda x: [ord(p[1]) - ord(p[0]) for p in zip(x, x[1:])])
        base = [ord(p[1]) - ord(p[0]) for p in zip(words[1], words[1][1:])]
        first = [ord(p[1]) - ord(p[0]) for p in zip(words[0], words[0][1:])]
        if first != base:
            return words[0]
        return words[-1]

s = Solution()
print(s.oddString(["adc","wzy","abc"]))
print(s.oddString(["aaa","bob","ccc","ddd"]))
