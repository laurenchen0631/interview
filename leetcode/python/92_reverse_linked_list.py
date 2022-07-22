# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy, head
        for _ in range(left-1):
            print(cur.val)
            prev, cur = cur, cur.next
        
        end, start = prev, cur
        for i in range(right-left+1):
            cur.next, cur, prev = prev, cur.next, cur

        end.next = prev
        start.next = cur
        return dummy.next 