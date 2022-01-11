# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        total: int = 0
        def dfs(root: TreeNode | None, n: int) -> None:
            nonlocal total
            n *= 2
            n += root.val

            if not root.left and not root.right:
                total += n
                return
            
            if root.left:
                dfs(root.left, n)
            if root.right:
                dfs(root.right, n)
        dfs(root, 0)
        return total

if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(0)
    r.right = TreeNode(1)

    s = Solution()
    print(s.sumRootToLeaf(r))