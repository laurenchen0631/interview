from package.LinkedList import LinkedList

def sum_reverse(lst1, lst2):
  sum_lst = []
  step = 0

  h1 = lst1.head
  h2 = lst2.head
  while h1 != None or h2 != None:
    n1 = h1.data if h1 else 0
    n2 = h2.data if h2 else 0
    acc = n1 + n2 + step
    if acc >= 10:
      step = 1
      acc -= 10
    else:
      step = 0
    
    sum_lst.append(acc)
    if h1:
      h1 = h1.next
    if h2:
      h2 = h2.next
  
  if step > 0:
    sum_lst.append(step)
  
  return LinkedList(sum_lst)

print(sum_reverse(LinkedList([4, 3, 2, 1]), LinkedList([8, 9, 9])))
print(sum_reverse(LinkedList([1, 1, 1]), LinkedList([9, 9, 9])))

def sum_list(lst1: LinkedList, lst2: LinkedList) -> LinkedList:
  if (n1 := lst1.len()) > (n2 := lst2.len()):
    lst2.head = padding(lst2.head, n1 - n2)
  else:
    lst1.head = padding(lst1.head, n2 - n1)
  
  (digits, carry) = sum_helper(lst1.head, lst2.head)
  lst = LinkedList([0])
  if carry == 0:
    lst.head = digits
  else:
    lst.head = insert_before(digits, carry)

  return lst

def sum_helper(h1: LinkedList.Node, h2: LinkedList.Node) -> (LinkedList.Node, int):
  if h1 == None and h2 == None:
    return (None, 0)
  
  (digits, carry) = sum_helper(h1.next, h2.next)
  val = carry + h1.data + h2.data
  return (insert_before(digits, val % 10), val // 10)

def padding(head, padding):
  for _ in range(padding):
    head = insert_before(head, 0)
  return head

def insert_before(head, val) -> LinkedList.Node:
  node = LinkedList.Node(val)
  node.next = head
  return node

print(sum_list(LinkedList([4, 3, 2, 1]), LinkedList([8, 9, 9])))
print(sum_list(LinkedList([9, 9, 9, 9]), LinkedList([1])))
