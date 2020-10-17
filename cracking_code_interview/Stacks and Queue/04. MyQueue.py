class MyQueue:
  def __init__(self):
    self.stack = []
    self.tmp_stack = []
  
  def queue(self, item):
    # self.__reverse_move(self.stack, self.tmp_stack)
    self.tmp_stack.append(item)
    # self.__reverse_move(self.tmp_stack, self.stack)
  
  def dequeue(self):
    if len(self.stack) == 0:
      self.__reverse_move(self.tmp_stack, self.stack)
    return self.stack.pop()
  
  def __reverse_move(self, source, target):
    while len(source) > 0:
      target.append(source.pop())

a = MyQueue()
a.queue(1)
a.queue(2)
a.queue(3)
a.queue(4)
print(a.dequeue())
a.queue(5)
print(a.dequeue())
