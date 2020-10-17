class MinStack:
  def __init__(self):
    self.__min_stack = []
    self.__stack = []
  
  def push(self, ele):
    if len(self.__min_stack) == 0 or ele <= self.__min_stack[-1]:
      self.__min_stack.append(ele)
    self.__stack.append(ele)
  
  def pop(self):
    top = self.__stack.pop()
    if top == self.__min_stack[-1]:
      self.__min_stack.pop()
    return top
  
  def min(self):
    return self.__min_stack[-1]

a = MinStack()
a.push(2)
a.push(6)
a.push(9)
a.push(5)
a.push(1)
a.push(4)
a.push(7)

print(a.min())
a.pop()
a.pop()
a.pop()
a.pop()
print(a.min())