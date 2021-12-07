# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        val: list[str] = []
        node = self
        while node != None:
            val.append(str(node.val))
            node = node.next
        return ' -> '.join(val)
      
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        val: int = 0
        node = head
        while node:
          val = (val * 2 + node.val)
          node = node.next
        return val