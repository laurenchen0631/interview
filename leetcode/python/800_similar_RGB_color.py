class Solution:
    # all shorthand is divisible by 17
    def similarRGB(self, color: str) -> str:
        res = ['#']
        for i in range(1, len(color), 2):
            c = color[i:i+2]
            n = int(c, 16)
            v = 17 * round(n / 17)
            res.append(hex(v)[2:].zfill(2))
        return ''.join(res)

s = Solution()
print(s.similarRGB('#09f166'))
print(s.similarRGB('#4e3fe1'))
print(s.similarRGB("#1c9e03"))