class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)
        return f'{x+y:b}'

if __name__ == '__main__':
    s = Solution()
    print(s.addBinary(a = "11", b = "1"))
    print(s.addBinary(a = "1010", b = "1011"))