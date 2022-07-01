class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1])
        res: int = 0
        while truckSize > 0 and boxTypes:
            n, units = boxTypes.pop()
            res += units * min(n, truckSize)
            truckSize -= n
        return res

s = Solution()
print(s.maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))
print(s.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10))