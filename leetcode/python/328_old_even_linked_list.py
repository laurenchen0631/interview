# Definition for singly-linked list.
from typing import overload


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
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head

        evenHead: ListNode | None = head.next
        oddNode: ListNode = head
        evenNode: ListNode | None = oddNode.next

        while True:
            nextOdd: ListNode | None = evenNode.next if evenNode else None
            if not nextOdd:
                break
            
            oddNode.next = nextOdd
            evenNode.next = nextOdd.next
            oddNode = nextOdd
            evenNode = nextOdd.next

        oddNode.next = evenHead
        return head
            
if __name__ == '__main__':
  s = Solution()
  l1 = ListNode(1)
  l1.next = ListNode(2)
  l1.next.next = ListNode(3)
  l1.next.next.next = ListNode(4)
  l1.next.next.next.next = ListNode(5)
  print(s.oddEvenList(l1))

  l2 = ListNode(1)
  l2.next = ListNode(3)
  l2.next.next = ListNode(5)
  l2.next.next.next = ListNode(7)
  print(s.oddEvenList(l2))