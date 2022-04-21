class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode | None):
        self.root = root
        self.stack: list[TreeNode] = []

    def next(self) -> int:
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        self.root = self.stack.pop()
        v = self.root.val
        self.root = self.root.right
        return v

    def hasNext(self) -> bool:
        return self.root or self.stack
