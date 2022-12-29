import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        sortedTasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        heap: list[tuple[int,int]] = []
        curTime = i = 0
        res = []
        while heap or i < len(tasks):
            if not heap and curTime < sortedTasks[i][0]:
                curTime = sortedTasks[i][0]
            while i < len(tasks) and sortedTasks[i][0] <= curTime:
                heapq.heappush(heap, (sortedTasks[i][1], sortedTasks[i][2]))
                i += 1
            
            t, idx = heapq.heappop(heap)
            curTime += t
            res.append(idx)
        return res