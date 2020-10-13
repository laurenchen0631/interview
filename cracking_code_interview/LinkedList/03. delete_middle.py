from package.LinkedList import LinkedList

def delete_node(n: LinkedList.Node) -> bool:
  if n == None or n.next == None:
    return False

  n.data = n.next.data
  n.next = n.next.next
  return True

# def delete_middle(lst: LinkedList):
#   if lst.head == None:
#     return

#   p1 = lst.head
#   p2 = lst.head
#   prev = None
#   while p2.next != None and p2.next.next != None:
#     prev = p1
#     p1 = p1.next
#     p2 = p2.next.next
  
#   if prev != None:
#     prev.next = prev.next.next

a = LinkedList([1, 2, 3, 4, 5, 6])
# delete_middle(a)
delete_node(a.head.next.next)
print(a)

d = LinkedList(['a', 'b', 'c', 'd', 'e'])
delete_node(d.head.next)
print(d)