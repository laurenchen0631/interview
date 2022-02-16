# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = node = ListNode()
        dummy.next = head
        while node.next and node.next.next:
            nextPair = node.next.next.next
            node.next.next.next = node.next
            node.next = node.next.next
            node = node.next.next
            node.next = nextPair
        return dummy.next
        
            
        