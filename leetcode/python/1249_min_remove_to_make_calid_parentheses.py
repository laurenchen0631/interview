class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack: list[str] = []
        for c in s:
            if c != ')':
                stack.append(c)
                continue
            tmp: str = ''
            while stack and stack[-1] != '(':
                tmp = stack.pop() + tmp
            if stack:
                stack[-1] = '(' + tmp + ')'
            else:
                stack.append(tmp)
        chars: list[str] = []
        for part in stack:
            if part != '(':
                chars.append(part)
        return ''.join(chars)

s = Solution()
print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
print(s.minRemoveToMakeValid("a)b(c)d"))
print(s.minRemoveToMakeValid("))(("))
