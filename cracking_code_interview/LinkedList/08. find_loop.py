from package.LinkedList import LinkedList

def find_loop(lst: LinkedList) -> LinkedList.Node:
  slow = lst.head
  fast = lst.head

  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      break
  
  # No loop
  if fast == None or fast.next == None:
    return None

  slow = lst.head
  while slow != fast:
    slow = slow.next
    fast = fast.next
  
  return slow

a = LinkedList([1, 2, 3, 4, 5])
a.head.next.next.next.next = a.head.next.next
print(find_loop(a))
