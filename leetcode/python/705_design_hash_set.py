class MyHashSet:
    def __init__(self):
        self.arr = [[] for _ in range(8)]
        self.len: int = 0

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.len += 1
        if self.len >= len(self.arr) // 2:
            self._migrate()
        i = self._hash(key)
        self.arr[i].append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        i = self._hash(key)
        self.arr[i].remove(key)
        self.len -= 1

    def contains(self, key: int) -> bool:
        i = self._hash(key)
        for n in self.arr[i]:
            if n == key:
                return True
        return False

    def _hash(self, k: int) -> int:
        return k % len(self.arr)

    def _migrate(self) -> None:
        arr = [[] for _ in range(len(self.arr) * 2)]
        for bucket in self.arr:
            for n in bucket:
                i = n % len(arr)
                arr[i].append(n)
        self.arr = arr

h = MyHashSet()
h.add(1)      
h.add(2)      
print(h.contains(1))
print(h.contains(3))
h.add(2)
print(h.contains(2))
h.remove(2)
print(h.contains(2))