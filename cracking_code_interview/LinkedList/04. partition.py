from package.LinkedList import LinkedList

def partition(lst, pivot):
  hl = LinkedList([0])
  pl = hl.head
  hr = LinkedList([0])
  pr = hr.head
  runner = lst.head
  
  while runner != None:
    if runner.data < pivot: 
      pl.next = runner
      pl = pl.next
    else:
      pr.next = runner
      pr = pr.next
    runner = runner.next
  pr.next = None

  if hl.head.next:
    pl.next = hr.head.next
    lst.head = hl.head.next
  else:
    lst.head = hr.head.next

def partition_opt(lst, pivot):
  pl = lst.head
  pr = lst.head
  runner = lst.head
  
  while runner != None:
    nxt = runner.next
    if runner.data < pivot: 
      # insert node at head
      runner.next = pl
      pl = runner
    else:
      pr.next = runner
      pr = runner
    runner = nxt
  pr.next = None

  lst.head = pl

a = LinkedList([7, 3, 5, 8, 5, 10, 2])
partition(a, 5)
print(a)

b = LinkedList([7, 3, 5, 8, 5, 10, 2])
partition_opt(b, 5)
print(b)