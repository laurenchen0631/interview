class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack: list[str] = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1] += c
                if len(stack[-1]) == k:
                    stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

s = Solution()
print(s.removeDuplicates(s = "abcd", k = 2))
print(s.removeDuplicates(s = "deeedbbcccbdaa", k = 3))
print(s.removeDuplicates(s = "pbbcggttciiippooaais", k = 2))