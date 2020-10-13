from package.LinkedList import LinkedList

def get_intersection(lst1: LinkedList, lst2: LinkedList) -> LinkedList.Node:
  nodes = set()
  n = lst2.head
  while n != None:
    nodes.add(n)
    n = n.next
  
  n = lst1.head
  while n != None:
    if n in nodes:
      return n
    n = n.next
  
  return None

def get_intersection_opt(lst1: LinkedList, lst2: LinkedList) -> LinkedList.Node:
  if lst1.head == None or lst2.head == None:
    return None

  (tail1, len1) = get_tail_and_length(lst1)
  (tail2, len2) = get_tail_and_length(lst2)
  if tail1 != tail2:
    return None

  short = lst1.head if len1 < len2 else lst2.head
  longer = lst2.head if len1 < len2 else lst1.head
  longer = advance_nodes(longer, abs(len1 - len2))

  while short != longer:
    short = short.next
    longer = longer.next
  
  return longer

def get_tail_and_length(lst: LinkedList) -> (LinkedList.Node, int):
  n = lst.head
  length = 1
  while n.next != None:
    n = n.next
    length += 1
  return (n, length)

def advance_nodes(head: LinkedList, k: int) -> LinkedList.Node:
  n = head
  for _ in range(k):
    n = n.next
  return n

a = LinkedList([1, 2, 3, 4, 5])
b = LinkedList([7, 8])
b.head.next.next = a.head.next.next.next
print(b)

n = get_intersection(a, b)
print(n.data)

m = get_intersection(a, b)
print(m.data)
