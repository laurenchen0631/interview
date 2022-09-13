from bisect import bisect_left, bisect_right


class HitCounter:
    def __init__(self):
        self.events: list[int] = []

    def hit(self, timestamp: int) -> None:
        self.events.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        start = timestamp - 300
        l = bisect_right(self.events, start)
        r = bisect_left(self.events, timestamp + 1)
        return r - l


# Your HitCounter object will be instantiated and called as such:
obj = HitCounter()
obj.hit(1)
obj.hit(2)
obj.hit(3)
print(obj.getHits(4))
obj.hit(300)
print(obj.getHits(300))
print(obj.getHits(301))
