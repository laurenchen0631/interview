class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1):
            return s
        res = ['']
        gap = 2 * numRows - 2
        for i in range(numRows):
            j = i
            t = gap - 2 * i
            while j < len(s):
                if t == 0:
                    t = gap
                res.append(s[j])
                j += t
                t = gap - t
        return ''.join(res)
    
s = Solution()
print(s.convert('PAYPALISHIRING', 3))
print(s.convert('PAYPALISHIRING', 4))