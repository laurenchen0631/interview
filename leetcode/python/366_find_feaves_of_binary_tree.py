# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findLeaves(self, root: TreeNode | None) -> list[list[int]]:
        children = dict[TreeNode, int]()
        parent: dict[TreeNode, TreeNode|None] = {root: None}
        stack = [root]
        q: list[TreeNode] = []
        while stack:
            p = stack.pop()
            if p.left:
                children[p] = children.get(p, 0) + 1
                parent[p.left] = p
                stack.append(p.left)
            if p.right:
                children[p] = children.get(p, 0) + 1
                parent[p.right] = p
                stack.append(p.right)
            if not p.left and not p.right:
                q.append(p)
        res: list[list[int]] = []
        while q:
            res.append([])
            tmp = []
            for p in q:
                res[-1].append(p.val)
                if not parent[p]: break # root
                children[parent[p]] -= 1
                if children[parent[p]] == 0:
                    tmp.append(parent[p])
        return res
        
        