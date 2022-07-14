class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        preCache: dict[int, int] = {}
        inCache: dict[int, int] = {}
        for i in range(len(preorder)):
            preCache[preorder[i]] = i
            inCache[inorder[i]] = i

        def dfs(preStart: int, preEnd: int, inStart: int, inEnd: int) -> TreeNode | None:
            if preStart > preEnd or inStart > inEnd:
                return None
            root = TreeNode(preorder[preStart])
            rootIndex = inCache[preorder[preStart]]
            leftLastIndex = preStart + rootIndex - inStart
            root.left = dfs(preStart + 1, leftLastIndex, inStart, rootIndex - 1)
            root.right = dfs(leftLastIndex + 1, preEnd, rootIndex + 1, inEnd)
            return root    
        
        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)