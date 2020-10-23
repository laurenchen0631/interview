from package.Tree import TreeNode

def is_balanced(root):
  (_, balanced) = get_height_and_balaned(root)
  return balanced

def get_height_and_balaned(root: TreeNode) -> (int, bool):
  if not root:
    return (0, True)
  if not root.left and not root.right:
      return (1, True)
  
  (left_height, left_balanced) = get_height_and_balaned(root.left)
  (right_height, right_balanced) = get_height_and_balaned(root.right)
  if not left_balanced or not left_balanced or abs(left_height - right_height) > 1:
    return (0, False)
  
  return (max(left_height, right_height) + 1, True)

root = TreeNode(0)
print(is_balanced(root))
root.left = TreeNode(1)
print(is_balanced(root))
root.left.left = TreeNode(2)
print(is_balanced(root))
root.right = TreeNode(3)
print(is_balanced(root))
