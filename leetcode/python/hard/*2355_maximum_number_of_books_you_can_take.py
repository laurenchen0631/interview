class Solution:
    # [3, 5, 7, 1, 1, 2, 5, 9]
    # [6, 5, 4, 3, 2, 1]
    def maximumBooks(self, books: list[int]) -> int:
        res = 0
        stack = []
        for i in range(len(books)):
            while stack and books[i] <= books[stack[-1][0]] + (i - stack[-1][0]):
                stack.pop()
            prev_end, prev_res = stack[-1] if stack else [-1, 0]
            h = min(i - prev_end, books[i])
            l1, l2 = books[i], books[i]-h+1
            cur = prev_res + (l1 + l2) * h // 2
            stack.append([i, cur])
            res = max(res, cur)
        return res