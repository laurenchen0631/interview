import heapq


class Solution:
    def connectSticks(self, sticks: list[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            tmp = heapq.heappop(sticks) + heapq.heappop(sticks)
            cost += tmp
            heapq.heappush(sticks, tmp)
        return cost

s = Solution()
print(s.connectSticks([3354,4316,3259,4904,4598,474,3166,6322,8080,9009]))