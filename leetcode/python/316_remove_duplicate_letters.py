class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack: list[str] = []
        used = set[str]()
        last = {c: i for i, c in enumerate(s)}
        
        for i, c in enumerate(s):
            if c in used:
                continue
            while stack and c < stack[-1] and i < last[stack[-1]]:
                used.discard(stack.pop())
            used.add(c)
            stack.append(c)
        return ''.join(stack)

s = Solution()
print(s.removeDuplicateLetters("bcabc"))
print(s.removeDuplicateLetters("cbacdcbc"))