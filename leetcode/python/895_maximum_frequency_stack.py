from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.numCounter = defaultdict(int)
        self.layerStack: list[list[int]] = []

    def push(self, val: int) -> None:
        self.numCounter[val] += 1
        if len(self.layerStack) < self.numCounter[val]:
            self.layerStack.append([val])
        else:
            self.layerStack[self.numCounter[val]-1].append(val)
        
    def pop(self) -> int:
        v = self.layerStack[-1].pop()
        if not self.layerStack[-1]:
            self.layerStack.pop()
        self.numCounter[v] -= 1
        return v


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())