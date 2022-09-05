from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: Node | None) -> list[list[int]]:
        if not root:
            return []
        res: list[list[int]] = [[]]
        q = deque([root, None])
        while q:
            node = q.popleft()
            if not node:
                if q:
                    res.append([])
                    q.append(None)
                continue
            res[-1].append(node.val)
            for child in node.children:
                q.append(child)
        return res