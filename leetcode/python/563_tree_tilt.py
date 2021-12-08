# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: TreeNode | None) -> int:
      return self._helper(root)[1]

    def _helper(self, root: TreeNode | None) -> tuple[int, int]:
      if not root:
        return (0, 0)
      
      leftRes = self._helper(root.left)
      rightRes = self._helper(root.right)
      sum = leftRes[0] + rightRes[0] + root.val
      diff = abs(leftRes[0] - rightRes[0])
      return (sum, diff + leftRes[1] + rightRes[1])

if __name__ == '__main__':
  s = Solution()
  t1 = TreeNode(1)
  t1.left = TreeNode(2)
  t1.right = TreeNode(3)

  print(s.findTilt(t1))

  t2 = TreeNode(21)
  t2.left = TreeNode(7)
  t2.right = TreeNode(14)
  t2.right.left = TreeNode(2)
  t2.right.right = TreeNode(2)
  t2.left.left = TreeNode(1)
  t2.left.right = TreeNode(1)
  t2.left.left.left = TreeNode(3)
  t2.left.left.right = TreeNode(3)

  print(s.findTilt(t2))
