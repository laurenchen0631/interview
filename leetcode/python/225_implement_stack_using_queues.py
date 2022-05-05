from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()
        self._top: int | None = None

    def push(self, x: int) -> None:
        self.q.appendleft(x)
        self._top = x

    def pop(self) -> int:
        tmp = deque()
        while len(self.q) > 1:
            self._top = self.q.pop()
            tmp.appendleft(self._top)
        v = self.q.pop()
        self.q = tmp
        return v

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return not self.q
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
s = MyStack()
s.push(1)
s.push(2)
print(s.pop())
print(s.top())
print(s.empty())