class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        k = len(num) - k
        res: int = 0
        if k <= 0:
            return '0'
        start: int = 0
        for _ in range(k):
            (i, d) = self.findMin(num, start, len(num)-k)
            res = res*10 + d
            start = i+1
            k -= 1
        return str(res)
    
    def findMin(self, num: str, start: int, end: int) -> tuple[int, int]:
        minimum = int(num[start])
        index = start
        for i in range(start+1, end+1):
            if (n := int(num[i])) < minimum:
                minimum = n
                index = i
        return (index, minimum)

s = Solution()
print(s.removeKdigits(num = "1432219", k = 3))
print(s.removeKdigits(num = "10200", k = 1))
print(s.removeKdigits(num = "10", k = 2))
