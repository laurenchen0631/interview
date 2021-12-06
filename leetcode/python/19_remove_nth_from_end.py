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
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        slow = head
        fast = head
        for _ in range(n):
          if not fast:
            return head
          fast = fast.next

        if not fast:
          return head.next
        
        while fast.next:
          slow = slow.next
          fast = fast.next
        slow.next = slow.next.next
        return head