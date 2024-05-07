# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # 1->8->9 becomes 3->7->8
    def doubleIt(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        dummy = ListNode(0, head)
        prev = dummy
        node = head
        while node:
            node.val = node.val * 2
            if node.val >= 10:
                node.val -= 10
                prev.val += 1
            prev = node
            node = node.next
        
        if dummy.val:
            return dummy
        return dummy.next
            
        
