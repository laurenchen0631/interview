import heapq


class SeatManager:

    def __init__(self, n: int):
        self._index = 1
        self.available_seats = []

    def reserve(self) -> int:
        if self.available_seats:
            n = heapq.heappop(self.available_seats)
            return n
        
        n = self._index
        self._index += 1
        return n
    
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available_seats, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)