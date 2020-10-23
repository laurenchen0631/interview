import random

class BinarySearchTree:
  class Node:
    def __init__(self, data):
      self.data = data
      self.__size = 1
      self.left = None
      self.right = None
    
    def get_ith_node(self, i: int):
      left_size = self.left.size() if self.left else 0
      if i < left_size:
        return self.left.get_ith_node(i)
      elif i == left_size:
        return self
      else:
        return self.right.get_ith_node(i - (left_size + 1))
      
    def insert(self, data):
      if data <= self.data:
        if self.left:
          self.left.insert(data)
        else:
          self.left = BinarySearchTree.Node(data)
      else:
        if self.right:
          self.right.insert(data)
        else:
          self.right = BinarySearchTree.Node(data)
      self.__size += 1

    def size(self): 
      return self.__size

  def __init__(self):
    self.root = None
  
  def insert(self, data):
    if self.root:
      self.root.insert(data)
    else:
      self.root = BinarySearchTree.Node(data)

  def get_random_node(self):
    if not self.root:
      return None

    # randint(a, b): a <= N <= b
    i = random.randint(0, self.size() - 1)
    return self.root.get_ith_node(i)

  def size(self):
    return self.root.size() if self.root else 0
      
t = BinarySearchTree()
t.insert(2)
t.insert(1)
t.insert(3)

print(t.get_random_node().data)