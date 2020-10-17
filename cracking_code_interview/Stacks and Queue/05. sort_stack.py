from package.Stack import Stack

def sort_stack(s: Stack):
  max_stack = Stack()
  while not s.is_empty():
    top = s.pop()
    while not max_stack.is_empty() and top < max_stack.peek():
      s.push(max_stack.pop())
    max_stack.push(top)
  
  while not max_stack.is_empty():
    s.push(max_stack.pop())

a = Stack([7, 9, 3, 1 ,5])
sort_stack(a)
print(a)
