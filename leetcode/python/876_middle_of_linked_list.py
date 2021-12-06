from typing import List


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
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        cur = head
        end = head
        while end and end.next:
          cur = cur.next
          end = end.next.next
        return cur
        
if __name__ == '__main__':
  s = Solution()
  l1 = ListNode(1)
  l1.next = ListNode(2)
  l1.next.next = ListNode(3)
  l1.next.next.next = ListNode(4)
  l1.next.next.next.next = ListNode(5)
  print(s.middleNode(l1).val)

  l2 = ListNode(1)
  l2.next = ListNode(2)
  l2.next.next = ListNode(3)
  l2.next.next.next = ListNode(4)
  print(s.middleNode(l2).val)

  l3 = ListNode(1)
  print(s.middleNode(l3).val)