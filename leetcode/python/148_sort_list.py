# Definition for singly-linked list.
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
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            if not fast or not fast.next:
                slow.next, slow = None, slow.next
            else:
                slow = slow.next
        l = self.sortList(head)
        r = self.sortList(slow)
        dummy = node = ListNode()
        while l and r:
            if l.val < r.val:
                node.next = l
                l = l.next
            else:
                node.next = r
                r = r.next
            node = node.next
        node.next = l if l else r
        return dummy.next

h = ListNode(4)
h.next = ListNode(2)
h.next.next = ListNode(1)
h.next.next.next = ListNode(3)

s = Solution()
print(s.sortList(h))