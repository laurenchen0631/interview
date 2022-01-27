class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col: int = 0
        for i in range(len(columnTitle)):
            c = columnTitle[len(columnTitle) - 1 - i]
            col += (ord(c) - ord('A') + 1) * 26 ** i
        return col

if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber('A'))
    print(s.titleToNumber('AB'))
    print(s.titleToNumber('ZY'))
    print(s.titleToNumber('FXSHRXW'))