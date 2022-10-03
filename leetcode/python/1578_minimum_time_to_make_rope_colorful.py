class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        res: int = 0
        i: int = 0
        while i < len(colors):
            curMax = total = neededTime[i]
            while i < len(colors) - 1 and colors[i] == colors[i+1]:
                i += 1
                total += neededTime[i]
                curMax = max(curMax, neededTime[i])
            i += 1
            res += total - curMax
        return res

s = Solution()
print(s.minCost(colors = "abaac", neededTime = [1,2,3,4,5]))
print(s.minCost(colors = "abc", neededTime = [1,2,3]))
print(s.minCost(colors = "aabaa", neededTime = [1,2,3,4,1]))