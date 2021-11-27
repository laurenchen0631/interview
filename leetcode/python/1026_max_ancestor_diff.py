class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def maxAncestorDiff(self, root: list[TreeNode]) -> int:
    # return self._helper(root, [])

    return self._helper2(root, root.val if root != None else 0, root.val if root != None else 0)

  def _helper(self, node: TreeNode | None, ancestors: list[int]) -> int:
    if node == None:
      return 0
    
    maxDiff = 0
    for n in ancestors:
      maxDiff = max(maxDiff, abs(node.val - n))

    return max(
      maxDiff,
      self._helper(node.left, ancestors + [node.val]),
      self._helper(node.right, ancestors + [node.val]),
    )

  def _helper2(self, node: TreeNode | None, maxVal: int, minVal: int) -> int:
    if node == None:
      return 0

    maxVal = max(maxVal, node.val)
    minVal = min(minVal, node.val)
    return max(
      maxVal - minVal,
      self._helper2(node.left, maxVal, minVal),
      self._helper2(node.right, maxVal, minVal),
    )


