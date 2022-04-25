class UndergroundSystem:
    def __init__(self):
        self.inStation: dict[int, tuple[str, int]] = {}
        self.records: dict[tuple[str, str], tuple[int, int]] = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.inStation[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.inStation:
            return
        
        (start, t1) = self.inStation[id]
        key = (start, stationName)
        if key not in self.records:
            self.records[key] = (1, t - t1)
        else:
            self.records[key] = (self.records[key][0]+1, self.records[key][1] + t - t1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        return self.records[key][1] / self.records[key][0]
        