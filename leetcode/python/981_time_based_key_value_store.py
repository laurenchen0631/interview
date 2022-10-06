from bisect import bisect, bisect_left


class TimeMap:
    def __init__(self):
        self.map: dict[str, list[tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ''
        values = self.map[key]
        if timestamp < values[0][0]:
            return ''
        if timestamp >= values[-1][0]:
            return values[-1][1]
        
        i = bisect_left(values, (timestamp, chr(127)))
        return values[i][1] if values[i][0] == timestamp else values[i-1][1]

