import math
from package.Tree import TreeNode

def create_min_bst(arr):
  return create_min_bst_helper(arr, 0, len(arr) - 1)

def create_min_bst_helper(arr, start, end):
  if end < start:
    return None

  middle = get_middle_index(start, end)
  node = TreeNode(arr[middle])
  node.left = create_min_bst_helper(arr, start, middle - 1)
  node.right = create_min_bst_helper(arr, middle + 1, end)
  return node

def get_middle_index(left, right):
  return left + math.ceil((right - left) / 2)

root = create_min_bst([1,2,3,4,5,6,7,8])
print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data)
print(root.left.left.left.data)
print(root.left.left.right)
