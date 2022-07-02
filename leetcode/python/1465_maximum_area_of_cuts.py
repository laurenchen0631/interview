class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        maxW = max(
            max([horizontalCuts[i] - horizontalCuts[i-1] for i in range(1, len(horizontalCuts))]) if len(horizontalCuts) > 1 else 0,
            horizontalCuts[0],
            h - horizontalCuts[-1]
        )
        maxH =  max(
            max([verticalCuts[i] - verticalCuts[i-1] for i in range(1, len(verticalCuts))]) if len(verticalCuts) > 1 else 0,
            verticalCuts[0],
            w - verticalCuts[-1]
        )

        return (maxW * maxH) % (10**9 + 7)

s = Solution()
print(s.maxArea(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]))
print(s.maxArea(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]))