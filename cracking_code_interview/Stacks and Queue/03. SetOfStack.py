class SetOfStack:
  def __init__(self, max_height):
    self._max_height = max_height
    self._stacks = [[]]
    self._cursor = 0
    self._height = 0

  def push(self, ele):
    if self._height == self._max_height:
      self._stacks.append([])
      self._cursor += 1
      self._height = 0
    self._stacks[self._cursor].append(ele)
    self._height += 1

  def pop(self):
    top = self._stacks[self._cursor].pop()
    self._height -= 1
    if self._height == 0:
      self._stacks = self._stacks[:self._cursor]
      self._cursor -= 1
      self._height = self._max_height
    return top

  def __repr__(self):
    return str(self._stacks)

a = SetOfStack(3)
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
print(a)
print(a.pop())
print(a.pop())
print(a.pop())
print(a)

class SetOfStackAlt:
  def __init__(self, max_height):
    self._max_height = max_height
    self._stacks = [[]]
    # self._cursor = 0
    self._height = 0

  def push(self, ele):
    if self._height == self._max_height:
      self._stacks.append([])
      # self._cursor += 1
      self._height = 0
    self._stacks[-1].append(ele)
    self._height += 1

  def pop(self):
    top = self._stacks[-1].pop()
    self._height -= 1
    if self._height == 0:
      self._stacks = self._stacks[:-1]
      self._height = self._max_height
    return top

  def __repr__(self):
    return str(self._stacks)

  def pop_at(self, index):
    top = self.__left_shift(index, True)
    self._height = len(self._stacks[-1])
    return top

  def __left_shift(self, index, at_top):
    removed = None
    if at_top:
      removed = self._stacks[index].pop()
    else:
      removed = self._stacks[index][0]
      self._stacks[index] = self._stacks[index][1:]

    if len(self._stacks[index]) == 0:
        self._stacks = self._stacks[0:index] + self._stacks[index + 1:]
    elif len(self._stacks[index]) > index + 1:
      val = self.__left_shift(index + 1, False)
      self._stacks[index].append(val)
    return removed

b = SetOfStackAlt(4)
b.push(1)
b.push(2)
b.push(3)
b.push(4)
b.push(5)
b.push(6)
b.push(7)
b.push(8)
b.push(9)
b.push(10)
print(b)
print(b.pop_at(1))
print(b)
print(b.pop_at(1))
print(b)