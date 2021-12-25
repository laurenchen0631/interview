from typing import Literal
class Solution:
    def calculate(self, s: str) -> int:
        stack: list[str | int] = [0, '+']
        symbols: set[str] = {'+', '-', '*', '/'}
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if s[i] in symbols:
                stack.append(s[i])
                i += 1
                continue
            print(stack)

            n = 0
            while i < len(s) and s[i].isdigit():
                n = n * 10 + int(s[i])
                i += 1

            symbol = stack[-1]
            if symbol == '*' or symbol == '/':
                stack.pop()
                n2 = stack.pop()
                stack.append(self.calc(n2, n , symbol))
            else:
                stack.append(n)
        
        res = 0
        symbol = '+'
        for c in stack:
            if c in symbols:
                symbol = c
            else:
                res = self.calc(res, c, symbol)
        return res
                

    
    def calc(self, a: int, b: int, symbol: Literal['+', '-', '*', '/']) -> int:
        match symbol:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                return a // b

if __name__ == '__main__':
    s = Solution()
    print(s.calculate('3+2*2'))
    print(s.calculate(' 3/2 '))
    print(s.calculate('3+5/2'))
    print(s.calculate('0-2147483647'))