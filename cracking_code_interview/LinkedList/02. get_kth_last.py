from package.LinkedList import LinkedList

def get_kth_last(lst: LinkedList, k: int):
  p1 = lst.head
  p2 = get_kth(lst, k)
  if p2 == None:
    raise IndexError()

  while p2.next != None:
    p1 = p1.next
    p2 = p2.next

  return p1.data

def get_kth(lst: LinkedList, k: int):
  runner = lst.head
  for i in range(k-1):
    if runner == None:
      return None
    runner = runner.next
  return runner

a = LinkedList([1, 2, 3, 4, 5, 6, 7])
print(get_kth_last(a, 1))
print(get_kth_last(a, 7))
try:
  print(get_kth_last(a, 8))
except IndexError as err:
  print("IndexError")

b = LinkedList([4])
print(get_kth_last(b, 1))