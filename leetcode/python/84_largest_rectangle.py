class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [-1]
        maxArea = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                j = stack.pop()
                width = i - stack[-1] - 1
                maxArea = max(maxArea, heights[j] * width)
            stack.append(i)

        while stack[-1] != -1:
            j = stack.pop()
            width = len(heights) - stack[-1] - 1
            maxArea = max(maxArea, heights[j] * width)
        return maxArea
 
s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
print(s.largestRectangleArea([2,4]))