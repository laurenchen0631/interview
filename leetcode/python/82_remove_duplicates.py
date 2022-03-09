class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = tail = ListNode()
        node = head
        while node:
            v = node.val
            if not node.next or node.next.val != v:
                tail.next = node
                tail = tail.next
            while node and node.val == v:
                node = node.next
        tail.next = None
        return dummy.next