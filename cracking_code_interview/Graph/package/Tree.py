class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.parent = None

  def __repr__(self):
    return str(self.data)

  def add_left(self, data):
    self.left = TreeNode(data)
    self.left.parent = self

  def add_right(self, data):
    self.right = TreeNode(data)
    self.right.parent = self
