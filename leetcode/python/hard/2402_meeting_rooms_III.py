import heapq
from multiprocessing import heap


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        unused_room = list(range(n))
        used_room = [] # (end, room)
        meeting_count = [0] * n
        for start, end in meetings:
            while used_room and used_room[0][0] <= start:
                _, room = heapq.heappop(used_room)
                heapq.heappush(unused_room, room)
            if unused_room:
                room = heapq.heappop(unused_room)
                heapq.heappush(used_room, (end, room))
            else:
                next_time, room = heapq.heappop(used_room)
                heapq.heappush(used_room, (next_time + end - start, room))
            meeting_count[room] += 1
        return meeting_count.index(max(meeting_count))