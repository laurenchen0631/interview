class MyHashMap:
    def __init__(self):
        self.arr = [list[tuple[int,int]]() for _ in range(8)]
        self.len: int = 0

    def put(self, key: int, value: int) -> None:
        i = self._hash(key)
        if res := self._exists(key):
            self.arr[i][res[0]] = (key, value)
            return
        
        self.len += 1
        self.arr[i].append((key, value))
        if self.len >= len(self.arr) // 2:
            self._migrate()

    def _exists(self, key: int) -> tuple[int, tuple[int, int]] | None:
        i = self._hash(key)
        for i, pair in enumerate(self.arr[i]):
            if pair[0] == key:
                return (i, pair)
        return None

    def get(self, key: int) -> int:
        if res := self._exists(key):
            return res[1][1]
        return -1

    def remove(self, key: int) -> None:
        i = self._hash(key)
        if res := self._exists(key):
            self.arr[i].remove(res[1])
    
    def _hash(self, key: int) -> int:
        return key % len(self.arr)

    def _migrate(self) -> None:
        arr = [[] for _ in range(len(self.arr) * 2)]
        for bucket in self.arr:
            for pair in bucket:
                i = pair[0] % len(arr)
                arr[i].append(pair)
        self.arr = arr

myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
print(myHashMap.get(1))
print(myHashMap.get(3))
myHashMap.put(2, 1)
print(myHashMap.get(2))
myHashMap.remove(2)
print(myHashMap.get(2))