class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        min = [(0,0), (0,0)] # (index, value)
        maxsize = 21 * len(costs)
        for cost in costs:
            tmp = [(0,maxsize), (0,maxsize)]
            for i, n in enumerate(cost):
                v = n + (min[1][1] if i == min[0][0] else min[0][1])
                if v < tmp[0][1]:
                    tmp[0], tmp[1] = (i, v), tmp[0]
                elif v >= tmp[0][1] and v < tmp[1][1]:
                    tmp[1] = (i, v)
                
            min = tmp

        return min[0][1]

s = Solution()
# print(s.minCost([[1,5,3],[2,9,4]]))
# print(s.minCost([[1,3],[2,4]]))
# print(s.minCost([[10,15,12,14,18,5],[5,12,18,13,15,8],[4,7,4,2,10,18],[20,9,9,19,20,5],[10,15,10,15,16,20],[9,6,11,10,12,11],[7,10,6,12,20,8],[3,4,4,18,10,2]]))
print(s.minCost([[1,2],[1,19],[17,13],[3,20],[20,16],[9,8],[2,7],[19,18],[14,1],[16,20],[5,8],[10,10],[1,15],[15,6],[16,13],[17,2],[11,16],[6,13],[5,7],[17,5],[16,13],[19,1]]))
