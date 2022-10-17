import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        heap = [intervals[0][1]]
        for start, end in intervals[1:]:
            if heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)

s = Solution()
print(s.minMeetingRooms(intervals = [[0,30],[5,10],[15,20]]))