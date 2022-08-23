# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        r = self.splitHalf(head)
        r = self.reverse(r)
        l = head
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
    
    def splitHalf(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
        return slow
    
    def reverse(self, head: ListNode | None) -> ListNode | None:
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev