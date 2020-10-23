from package.Tree import TreeNode

def is_bst(root):
  return is_bst_helper(root, None, None)

def is_bst_helper(root, min, max):
  if not root:
    return True
  
  if (min != None and root.data <= min) or (max != None and max < root.data):
    return False
  
  if not is_bst_helper(root.left, min, root.data) or not is_bst_helper(root.right, root.data, max):
    return False
  
  return True

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
print(is_bst(a))

b = TreeNode(10)
b.left = TreeNode(5)
b.right = TreeNode(15)
print(is_bst(b))
b.left.right = TreeNode(15)
print(is_bst(b))