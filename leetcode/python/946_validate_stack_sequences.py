class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack: list[int] = []
        popIndex: int = 0
        for v in pushed:
            stack.append(v)
            while popIndex < len(popped) and stack and stack[-1] == popped[popIndex]:
                stack.pop()
                popIndex += 1
        return len(stack) == 0

s = Solution()
print(s.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))
print(s.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2]))
print(s.validateStackSequences(pushed = [0, 1], popped = [0, 1]))