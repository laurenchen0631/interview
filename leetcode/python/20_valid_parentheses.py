class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack: list[str] = []
        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

s = Solution()
print(s.isValid(s = "()"))
print(s.isValid(s = "()[]{}"))
print(s.isValid(s = "(]"))