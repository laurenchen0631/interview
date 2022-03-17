class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
                continue
            v: int = 0
            while (t := stack.pop()) != '(':
                v += t
            stack.append(max(2*v, 1))
        return sum(stack)

s = Solution()
print(s.scoreOfParentheses('()'))
print(s.scoreOfParentheses('()()'))
print(s.scoreOfParentheses('(())'))
print(s.scoreOfParentheses('(()())'))
print(s.scoreOfParentheses('()(()())'))