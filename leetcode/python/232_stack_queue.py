from typing import Generic, TypeVar


T = TypeVar('T')

class MyQueue(Generic[T]):

  def __init__(self):
    self._tmpStack: list[T] = []
    self._queue: list[T] = []

  def push(self, x: T) -> None:
    self._tmpStack.append(x)

  def pop(self) -> T:
    if len(self._queue) == 0:
      self._transferTmpStack()
    return self._queue.pop()

  def peek(self) -> T:
    if len(self._queue) == 0:
      self._transferTmpStack()
    return self._queue[-1]

  def empty(self) -> bool:
    return len(self._tmpStack) + len(self._queue) == 0

  def _transferTmpStack(self) -> None:
    while len(self._tmpStack) > 0:
      self._queue.append(self._tmpStack.pop())
        
if __name__ == '__main__':
  q = MyQueue[int]()
  q.push(1)
  q.push(2)
  print(q.peek())
  print(q.pop())
  print(q.empty())