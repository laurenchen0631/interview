from bisect import bisect_left


class SummaryRanges:
    def __init__(self):
        self.intervals: list[list[int]] = []

    def addNum(self, value: int) -> None:
        i = bisect_left(self.intervals, value, key=lambda x: x[0])
        if (i > 0 and self.intervals[i-1][1] >= value) or (i < len(self.intervals) and self.intervals[i][0] <= value):
            return 
        
        mergeLeft = i > 0 and self.intervals[i-1][1] == value - 1
        mergeRight = i < len(self.intervals) and self.intervals[i][0] == value + 1
        
        if mergeLeft and mergeRight:
            self.intervals[i-1][1] = self.intervals[i][1]
            self.intervals.pop(i)
        elif mergeLeft:
            self.intervals[i-1][1] = value
        elif mergeRight:
            self.intervals[i][0] = value
        else:
            self.intervals.insert(i, [value, value])
    
    def getIntervals(self) -> list[list[int]]:
        return self.intervals

s = SummaryRanges()
s.addNum(1)
print(s.getIntervals())
s.addNum(3)
print(s.getIntervals())
s.addNum(0)
print(s.getIntervals())
s.addNum(7)
print(s.getIntervals())
s.addNum(4)
print(s.getIntervals())

s.addNum(2)
print(s.getIntervals())
s.addNum(2)
print(s.getIntervals())
