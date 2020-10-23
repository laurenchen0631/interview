from package.Tree import TreeNode

def is_subtree(t1: TreeNode, t2: TreeNode) -> bool:
  if t2 == None:
    return True
  return is_subtree_helper(t1, t2)

def is_subtree_helper(t1: TreeNode, t2: TreeNode) -> bool:
  if t1 == None:
    return False
  elif t1.data == t2.data and match_tree(t1, t2):
    return True
  
  return is_subtree_helper(t1.left, t2) or is_subtree_helper(t1.right, t2)

def match_tree(t1: TreeNode, t2: TreeNode) -> bool:
  if t1 == None and t2 == None:
    return True
  elif t1 == None or t2 == None:
    return False
  elif t1.data != t2.data:
    return False
  return match_tree(t1.left, t2.left) and match_tree(t1.right, t2.right)

t1 = TreeNode(1)
t1.add_left(2)
t1.add_right(3)
t1.left.add_left(4)
t1.left.add_left(5)

t2 = TreeNode(2)
t2.add_left(4)
t2.add_right(5)

print(is_subtree(t1, t2))