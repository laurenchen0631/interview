from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self._total = 0
        self._size = size
        self._q = deque([])

    def next(self, val: int) -> float:
        self._total += val
        self._q.append(val)
        if len(self._q) > self._size:
            oldest = self._q.popleft()
            self._total -= oldest
        return self._total / len(self._q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)