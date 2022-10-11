import heapq


class MaxStack:
    def __init__(self):
        self._stack: list[tuple[int,int]] = []
        self._heap: list[tuple[int,int]] = []
        self._id = 0
        self._removedStack = set[int]()
        self._removedHeap = set[int]()

    def push(self, x: int) -> None:
        self._stack.append((x, self._id))
        heapq.heappush(self._heap, (-x, -self._id))
        self._id += 1

    def pop(self) -> int:
        self.top()
        v, id = self._stack.pop()
        self._removedStack.add(id)
        return v

    def top(self) -> int:
        while self._stack and self._stack[-1][1] in self._removedHeap:
            id = self._stack.pop()[1]
            self._removedHeap.remove(id)
        return self._stack[-1][0]
        

    def peekMax(self) -> int:
        while -self._heap[0][1] in self._removedStack:
            id = -heapq.heappop(self._heap)[1]
            self._removedStack.remove(id)
        return -self._heap[0][0]

    def popMax(self) -> int:
        v = self.peekMax()
        id = -heapq.heappop(self._heap)[1]
        self._removedHeap.add(id)
        return v
        
stk = MaxStack()
stk.push(5)  
stk.push(1)  
stk.push(5)
print(stk.top())
print(stk.popMax())
print(stk.top())
print(stk.peekMax())
print(stk.pop())
print(stk.top())
