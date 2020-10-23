
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
    self.end = n

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
      self.end = end
      return

    self.end.next = end
    self.end = self.end.next

  def __len__(self) -> int:
    length = 0
    n = self.head
    while n != None:
      length += 1
      n = n.next
    return length

  def __iter__(self):
    n = self.head
    while n != None:
      yield n.data
      n = n.next

if __name__ == '__main__':
  a = LinkedList([3, 5])
  a.append(2)
  print(a)

  b = LinkedList([])
  b.append(1)
  b.append(2)
  print(b)
