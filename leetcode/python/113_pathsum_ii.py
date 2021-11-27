# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
    res: list[list[int]] = []
    self.helper(root, targetSum, [], res)
    return res

  def helper(self, root: TreeNode | None, targetSum: int, path: list[int], result: list[list[int]]) -> None:
    if not root:
      return

    if not root.left and not root.right:
      if targetSum == root.val:
        result.append(path.copy())
        result[-1].append(root.val)
      return

    path.append(root.val)
    if root.left:
      self.helper(root.left, targetSum - root.val, path, result)
    if root.right:
      self.helper(root.right, targetSum - root.val, path, result)
    path.pop()
