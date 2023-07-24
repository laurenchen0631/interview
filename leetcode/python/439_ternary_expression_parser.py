class Solution:
    def parseTernary(self, expression: str) -> str:
        if len(expression) == 1:
            return expression
        stack = ['?']
        i = 2
        while stack:
            if expression[i] == '?':
                stack.append('?')
            elif expression[i] == ':':
                stack.pop()
            i += 1
        return self.parseTernary(expression[2:i - 1]) if expression[0] == 'T' else self.parseTernary(expression[i:])
