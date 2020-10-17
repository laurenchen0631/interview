class Queue:
  def __init__(self, it = []):
    self._data: list = []
    for item in it:
      self._data.append(item)

  def __repr__(self):
    return str(self._data)
  
  def remove(self):
    val = self._data[0]
    self._data = self._data[1:]
    return val

  def add(self, ele):
    self._data.append(ele)

  def peek(self):
    return self._data[0]

  def is_empty(self):
    return len(self._data)

if __name__ == '__main__':
  s = Queue()
  s.add(1)
  s.add(2)
  s.add(3)
  print(s.peek())
  print(s.remove())
  print(s.remove())
  print(s.remove())
  print(s.is_empty())
  # print(s.remove())
  
  try:
    s.peek()
  except Exception as err:
    print(err)
