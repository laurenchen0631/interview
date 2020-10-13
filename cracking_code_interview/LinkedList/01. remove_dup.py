from package.LinkedList import LinkedList

# time: O(N) space: O(N)
def remove_dup(a: LinkedList):
  n: LinkedList.Node = a.head
  if n == None:
    return

  data = set([n.data])
  while n.next != None:
    if n.next.data in data:
      n.next = n.next.next
    else:
      data.add(n.next.data)
      n = n.next

# time: O(N^2) space: O(1)
def remove_dup2(a: LinkedList):
  flag: LinkedList.Node = a.head
  if flag == None:
    return
  
  while flag != None:
    runner = flag
    while runner.next != None:
      if runner.next.data == flag.data:
        runner.next = runner.next.next
      else:
        runner = runner.next
    flag = flag.next
  
a = LinkedList([1, 2, 2, 1])
remove_dup(a)
print(a)

b = LinkedList([7, 5, 5, 3, 1, 5, 1])
remove_dup(b)
print(b)

c = LinkedList([1, 2, 2, 1])
d = LinkedList([7, 5, 5, 3, 1, 5, 1])
remove_dup2(c)
remove_dup2(d)

print(c)
print(d)