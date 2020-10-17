

class LinkedList:
  class Node:
    """
    Linked List Node
    """
    def __init__(self, data):
      self.data = data
      self.next: LinkedList.Node = None

  def __init__(self, it):
    sentinel = LinkedList.Node(0)
    n = sentinel
    for d in it:
      n.next = LinkedList.Node(d)
      n = n.next
    self.head = sentinel.next

  def __repr__(self):
    values = []
    n = self.head
    while n != None:
      values.append(str(n.data))
      n = n.next
    return ' -> '.join(values)
  
  def append(self, data):
    end = LinkedList.Node(data)
    if self.head == None:
      self.head = end
      return
    
    n = self.head
    while n.next != None:
      n = n.next
    n.next = end

  def delete(self, data):
    if self.head == None:
      return
    
    n = self.head
    if n.data == data:
      self.head = self.head.next
      return
    
    while n.next != None:
      if n.next.data == data:
        n.next = n.next.next
        return
      n = n.next

  def len(self) -> int:
    length = 0
    n = self.head
    while n != None:
      length += 1
      n = n.next
    return length
