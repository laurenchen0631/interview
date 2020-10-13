from package.LinkedList import LinkedList

def is_palindrome(lst) -> bool:
  stack = []
  slow = lst.head
  fast = lst.head
  while fast != None and fast.next != None:
    stack.append(slow.data)
    slow = slow.next
    fast = fast.next.next
  
  is_odd_elements = fast != None
  if is_odd_elements:
    slow = slow.next # skip the middle one
  
  while slow != None:
    if stack.pop() != slow.data:
      return False
    slow = slow.next
  return True

print(is_palindrome(LinkedList([1, 2, 3, 2, 1])))
print(is_palindrome(LinkedList([1, 2, 3])))
print(is_palindrome(LinkedList([2, 2])))