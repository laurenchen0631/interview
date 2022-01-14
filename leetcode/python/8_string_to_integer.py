class Solution:
    def __init__(self):
        self.nums: dict[str, int] = {}
        self.intMax = 2**31 - 1
        self.intMin = -2**31
        for i in range(0, 10):
            self.nums[str(i)] = i

    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return 0

        sign: -1 | 1 = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            i += 1
            sign = -1
        
        n: int = 0
        while i < len(s) and s[i] in self.nums:
            n = n*10 + self.nums[s[i]]
            i += 1
        n = sign * n
        if n > self.intMax:
            return self.intMax
        elif n < self.intMin:
            return self.intMin
        return n
        

s = Solution()
print(s.myAtoi("42"))
print(s.myAtoi("    -42"))
print(s.myAtoi("4193 with words"))
print(s.myAtoi("-91283472332"))
print(s.myAtoi("91283472332"))
