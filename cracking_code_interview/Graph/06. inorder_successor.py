from package.Tree import TreeNode

def inorder_successor(node: TreeNode):
  if node.right:
    return get_left_most(node.right)
  else:
    return get_unvisited_parent(node)

def get_left_most(root: TreeNode):
  n = root
  while n.left != None:
    n = n.left
  return n

def get_unvisited_parent(node: TreeNode):
  n: TreeNode = node
  parent: TreeNode = node.parent

  if parent != None and parent.left != n:
    n = parent
    parent = parent.parent
  return parent

root = TreeNode(1)
root.add_left(2)
root.add_right(3)
root.left.add_left(4)
root.left.add_right(5)

print(inorder_successor(root.left))
print(inorder_successor(root.left.left))
print(inorder_successor(root.left.right))