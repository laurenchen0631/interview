import random

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  
class Solution:

  def __init__(self, head: ListNode | None):
    self.cache: list[int] = []
    while head:
      self.cache.append(head.val) 
      head = head.next 

  def getRandom(self) -> int:
    return random.choice(self.cache)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()