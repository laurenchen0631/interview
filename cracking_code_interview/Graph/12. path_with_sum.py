from package.Tree import TreeNode

def count_path_equal(root, target):
  return count_sum_helper(root, target, [])

def count_sum_helper(root, target, sums):
  if not root:
    return 0

  add(sums, root.data)
  sums.append(root.data)
  count = has(sums, target) + count_sum_helper(root.left, target, sums) + count_sum_helper(root.right, target, sums)
  sums.pop()
  decrease(sums, root.data)

  return count

def add(arr, val):
  for i in range(len(arr)):
    arr[i] += val

def decrease(arr, val):
  for i in range(len(arr)):
    arr[i] -= val

def has(arr, val):
  count = 0
  for item in arr:
    if item == val:
      count += 1
  return count

root = TreeNode(8)
root.add_left(-4)
root.add_right(4)
root.left.add_left(6)
root.left.add_right(10)
root.left.right.add_left(7)
root.right.add_left(-6)
root.right.add_right(-10)
root.right.right.add_left(4)

print(count_path_equal(root, 6))