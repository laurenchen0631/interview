from package.Tree import TreeNode

def all_sequences(root): 
  result: list[list[TreeNode]] = []

  if root == None:
    result.append([])
    return result

  prefix: list[TreeNode] = [root.data]

  left_seq: list[list[TreeNode]] = all_sequences(root.left)
  right_seq: list[list[TreeNode]] = all_sequences(root.right)

  ## weave left and right
  for left in left_seq:
    for right in right_seq:
      weaved: list[list[TreeNode]] = []
      weave(left, right, weaved, prefix)
      print(weaved)
      result.extend(weaved)
  return result

def weave(left, right, results, prefix):
  if len(left) == 0 or len(right) == 0:
    results.append(list(prefix))
    results[-1].extend(left)
    results[-1].extend(right)
    return
  
  prefix.append(left[0])
  weave(left[1:], right, results, prefix)
  prefix.pop()

  prefix.append(right[0])
  weave(left, right[1:], results, prefix)
  prefix.pop()

root = TreeNode(50)
root.add_left(20)
root.add_right(60)
root.left.add_left(10)
root.left.add_right(25)
# root.left.left.add_left(5)
# root.left.left.add_right(15)
# root.right.add_right(70)
# root.right.right.add_left(65)
# root.right.right.add_right(80)

print(all_sequences(root))