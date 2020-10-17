class MultiStack:

  class StackInfo:
    def __init__(self, start, capacity):
      self.start = start
      self.capacity = capacity
      self.size = 0
    
    def is_valid_index(self, index, total_capacity):
      if index < 0 or index >= total_capacity:
        return False
      
      # If index wraps around, adjust it
      contiguous_index = index + total_capacity if index < self.start else index
      end = self.start + self.capacity
      return self.start <= contiguous_index and contiguous_index < end

    def last_capacity_index(self, total_capacity):
      return (self.start + self.capacity - 1) % total_capacity

    def last_element_index(self, total_capacity):
      return (self.start + self.size - 1) % total_capacity

    def is_full(self):
      return self.size == self.capacity
    
    def is_empty(self):
      return self.size == 0

  def __init__(self, default_size, num_stacks = 3):
    self._values = [None for _ in range(num_stacks * default_size)]
    print(self._values, len(self._values))
    self._info: list[MultiStack.StackInfo] = []
    for i in range(num_stacks):
      self._info.append(MultiStack.StackInfo(default_size * i, default_size))
    
  def push(self, stack_index: int, ele):
    if self.__is_full():
      raise Exception("Out of space")
      
    stack: MultiStack.StackInfo = self._info[stack_index]
    if stack.is_full():
      self.__expand(stack_index)
    
    stack.size += 1
    self._values[stack.last_element_index(len(self._values))] = ele
    
  def pop(self, stack_index: int):
    stack: MultiStack.StackInfo = self._info[stack_index]
    if stack.is_empty():
      raise Exception("pop empty stack")
    
    val = self._values[stack.last_element_index(len(self._values))]
    self._values[stack.last_element_index(len(self._values))] = None
    stack.size -= 1
    return val

  def peek(self, stack_index: int):
    stack: MultiStack.StackInfo = self._info[stack_index]
    return self._values[stack.last_element_index(len(self._values))]

  def __is_full(self):
    size = 0
    for info in self._info:
      size += info.size
    print(size, len(self._values))
    return size == len(self._values)
  
  def __expand(self, stack_index: int):
    self.__shift((stack_index + 1) % len(self._info))
    self._info[stack_index].capacity += 1

  def __shift(self, stack_index: int):
    print("Shifting ", stack_index)
    stack: MultiStack.StackInfo = self._info[stack_index]

    # If the stack is at its full capacity, then you need to move the next stack over by one element
    if (stack.size >= stack.capacity):
      self.__shift((stack_index + 1) % len(self._info))
      stack.capacity += 1

    # Shift all elements in stack over by one
    index = stack.last_capacity_index(len(self._values))
    while stack.is_valid_index(index, len(self._values)):
      prev_index = (index - 1) % len(self._values)
      self._values[index] = self._values[prev_index]
      index = prev_index

    self._values[stack.start] = None
    stack.start = (index + 1) % len(self._values)
    stack.capacity -= 1

a = MultiStack(2, 3)
a.push(0, 1)
a.push(0, 1)
a.push(0, 1)