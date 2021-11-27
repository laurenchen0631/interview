class OrderedStream:
  def __init__(self, n: int):
    self.stream: list[str | None] = [None] * n
    self._lastSent = 0

  def insert(self, idKey: int, value: str) -> list[str]:
    index = idKey - 1
    self.stream[index] = value

    if index == self._lastSent:
      for i in range(index, len(self.stream)):
        if self.stream[i] == None:
          self._lastSent = i
          return self.stream[index:self._lastSent]
      return self.stream[index:]

    return []

if __name__ == '__main__':
  s = OrderedStream(5)
  print(s.insert(3, 'ccccc'))
  print(s.insert(1, 'aaaaa'))
  print(s.insert(2, 'bbbbbb'))
  print(s.insert(5, 'eeeeee'))
  print(s.insert(4, 'dddddd'))
