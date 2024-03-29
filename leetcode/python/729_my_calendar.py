class Node:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node) ->  bool:
        if node.start >= self.end:
            if self.right is None:
                self.right = node
                return True
            return self.right.insert(node)
        if node.end <= self.start:
            if self.left is None:
                self.left = node
                return True
            return self.left.insert(node)
        return False

                    
class MyCalendar:

    def __init__(self):
        self.root: Node | None = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
        return self.root.insert(Node(start, end))


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)