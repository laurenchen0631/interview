class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count: dict[str, int] = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) - 1
            count[t[i]] = count.get(t[i], 0) + 1
        count[t[-1]] = count.get(t[-1], 0) + 1
        for (c, n) in count.items():
            if n > 0:
                return c
        return ''

s = Solution()
print(s.findTheDifference(s = "abcd", t = "abcde"))
print(s.findTheDifference(s = "", t = "y"))