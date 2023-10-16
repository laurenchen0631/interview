class Solution:
    # [3, 5, 7, 1, 1, 2, 5, 9]
    # [6, 5, 4, 3, 2, 1]
    def maximumBooks(self, books: list[int]) -> int:
        n = len(books)

        def calculateSum(l: int, r: int) -> int:
            h = min(books[r], r - l + 1) # [2, 0]
            bottom = books[r] - h + 1

            return (books[r] + bottom) * h // 2
        
        stack = []
        dp = [0] * n

        for i, book in enumerate(books):
            # While we cannot push i, we pop from the stack
            while stack and books[stack[-1]] - stack[-1] >= book - i:
                stack.pop()
            
            if not stack:
                dp[i] = calculateSum(0, i)
            else:
                j = stack[-1]
                dp[i] = dp[j] + calculateSum(j+1, i)
            stack.append(i)
        
        return max(dp)
