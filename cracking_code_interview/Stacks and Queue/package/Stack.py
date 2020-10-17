class Stack:
  def __init__(self, it = []):
    self._data: list = []
    for item in it:
      self._data.append(item)

  def __repr__(self):
    return str(self._data)
  
  def pop(self):
    return self._data.pop()

  def push(self, ele):
    return self._data.append(ele)

  def peek(self):
    return self._data[-1]

  def is_empty(self):
    return len(self._data) == 0

if __name__ == '__main__':
  s = Stack()
  s.push(1)
  s.push(2)
  s.push(3)
  print(s.peek())
  print(s.pop())
  print(s.pop())
  print(s.pop())
  print(s.is_empty())
  # print(s.pop())
  
  try:
    s.peek()
  except Exception as err:
    print(err)
