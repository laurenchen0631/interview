import heapq


class MedianFinder:
    def __init__(self):
        self._upper: list[int] = [] # min heap
        self._lower: list[int] = [] # max heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self._upper, num)
        heapq.heappush(self._lower, -heapq.heappop(self._upper))

        if len(self._upper) < len(self._lower):
            heapq.heappush(self._upper, -heapq.heappop(self._lower))

        print(self._upper, self._lower)

    def findMedian(self) -> float:
        if len(self._upper) == len(self._lower):
            return (self._upper[0] - self._lower[0]) / 2
        return self._upper[0]

medianFinder = MedianFinder();
# ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
# [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]
medianFinder.addNum(-1)
print(medianFinder.findMedian())
medianFinder.addNum(-2)
print(medianFinder.findMedian())
medianFinder.addNum(-3)
print(medianFinder.findMedian())
medianFinder.addNum(-4)
print(medianFinder.findMedian())
medianFinder.addNum(-5)
print(medianFinder.findMedian())
