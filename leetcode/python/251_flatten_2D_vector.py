
class Vector2D:
    def __init__(self, vec: list[list[int]]):
        self._vec = vec
        self._vec.reverse()
        self._i = 0

    def next(self) -> int:
        if not self.hasNext():
            return None
        if self._i == len(self._vec[-1]):
            self._vec.pop()
            self._i = 0
        v = self._vec[-1][self._i]
        self._i += 1
        return v

    def hasNext(self) -> bool:
        if not self._vec:
            return False
        if self._i < len(self._vec[-1]):
            return True
        tmp = self._vec.pop()
        while self._vec and not self._vec[-1]:
            self._vec.pop()
        self._vec.append(tmp)
        return len(self._vec) > 1

s = Vector2D([[1,2],[3],[4]])
print(s.next())
print(s.next())
print(s.next())
# print(s.next())
print(s.hasNext())
print(s.next())
print(s.hasNext())

