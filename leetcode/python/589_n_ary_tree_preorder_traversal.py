class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children: list[Node] | None = children

class Solution:
    def preorder(self, root: Node | None) -> list[int]:
        if not root:
            return []
        res: list[int] = []
        stack: list[Node] = [root]
        while stack:
            p = stack.pop()
            res.append(p.val)
            if p.children:
                stack.extend(p.children[::-1])
        return res
        