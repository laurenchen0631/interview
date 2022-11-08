class Solution:
    def makeGood(self, s: str) -> str:
        res: list[str] = []
        for c in s:
            if res and c.lower() == res[-1].lower() and c != res[-1]:
                res.pop()
            else:
                res.append(c)
        return ''.join(res)

s = Solution()
print(s.makeGood("leEeetcode"))