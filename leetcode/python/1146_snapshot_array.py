from bisect import bisect_right


class SnapshotArray:
    def __init__(self, length: int):
        self.id = 0
        self.records = [[[self.id, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.records[index][-1][0] == self.id:
            self.records[index][-1][1] = val
        else:
            self.records[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect_right(self.records[index], snap_id, key=lambda x: x[0])
        return self.records[index][i][1]
        
