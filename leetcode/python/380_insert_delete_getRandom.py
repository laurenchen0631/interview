import random

class RandomizedSet:
    def __init__(self):
        self._map = dict[int, int]()
        self._list = list[int]()

    def insert(self, val: int) -> bool:
        if val in self._map:
            return False
        self._map[val] = len(self._list)
        self._list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._map:
            return False
        last = self._list[-1]
        idx = self._map[val]
        self._list[idx] = last
        self._map[last] = idx
        self._list.pop()
        del self._map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self._list)
