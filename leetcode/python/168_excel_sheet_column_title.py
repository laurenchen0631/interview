class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, d = divmod(columnNumber, 26)
            res.append(chr(d + ord('A')))
        return ''.join(reversed(res))