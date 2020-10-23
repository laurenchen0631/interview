from package.Tree import TreeNode
import queue

def common_ancestor(a: TreeNode, b: TreeNode):
  delta = depth(a) - depth(b)
  p = b if delta > 0 else a
  q = a if delta > 0 else b
  q = ascend(q, abs(delta))

  while p != q and p != None and q != None:
    p = p.parent
    q = q.parent

  return None if p == None or q == None else p

def depth(node):
  depth = 0
  while node != None:
    node = node.parent
    depth += 1
  return depth

def ascend(node, step):
  while step > 0 and node != None:
    node = node.parent
    step -= 1
  return node

root = TreeNode(5)
root.add_left(10)
root.add_right(9)
root.left.add_left(2)
root.left.add_right(3)
root.right.add_right(8)

print(common_ancestor(root.left.left, root.left.right))
print(common_ancestor(root.left.left, root.right.right))