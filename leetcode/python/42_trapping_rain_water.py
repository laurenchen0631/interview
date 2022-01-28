class Solution:
    def trap(self, height: list[int]) -> int:
        res: int = 0
        curMaxIndex: int = 0
        blocks: int = 0
        for i in range(1, len(height)):
            if height[curMaxIndex] <= height[i]:
                res += (i - curMaxIndex - 1) * height[curMaxIndex] - blocks
                curMaxIndex = i
                blocks = 0
            else:
                blocks += height[i]
        
        curMaxIndex = len(height) - 1
        blocks = 0
        for i in range(len(height) - 2, -1, -1):
            # Exclude the same case from left to right 
            if height[curMaxIndex] < height[i]:
                res += ((curMaxIndex - i - 1) * height[curMaxIndex] - blocks)
                curMaxIndex = i
                blocks = 0
            else:
                blocks += height[i]
        return res

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))