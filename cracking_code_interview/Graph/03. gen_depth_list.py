from package.Tree import TreeNode
from package.LinkedList import LinkedList
import queue

# def gen_depth_list(root):
#   q: queue.Queue = queue.Queue()
#   q.put(root)
#   lst = []
#   level_counter = 1
#   head = end = LinkedList.Node(0)

#   while not q.empty():
#     node = q.get()
#     end.next = LinkedList.Node(node)
#     end = end.next

#     if node.left:
#       q.put(node.left)
#     if node.right:
#       q.put(node.right)
    
#     level_counter -= 1
#     if level_counter == 0:
#       lst.append(head.next)
#       head = end = LinkedList.Node(0)
#       level_counter = q.qsize()

#   return lst

def gen_depth_list(root):
  if not root:
    return []
  
  q: queue.Queue = queue.Queue()
  q.put(root)
  lst = []
  current = LinkedList([root])

  while len(current) > 0:
    lst.append(current)
    parents = current
    current = LinkedList([])

    for parent in parents:
      if parent.left:
        current.append(parent.left)
      if parent.right:
        current.append(parent.right)

  return lst

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(4)
root.left.left.right = TreeNode(5)

lst = gen_depth_list(root)
print(lst)