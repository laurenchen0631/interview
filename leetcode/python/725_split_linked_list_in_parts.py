class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        res: list[ListNode | None] = [None] * k
        if not head:
            return res
        
        n = self.count(head)
        width, remainder = divmod(n, k) # 11, 3 -> 4, 4, 3 
        curr: ListNode | None = head
        for i in range(k):
            res[i] = curr
            # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
            for _ in range(width + (i < remainder) - 1): # -1 for the last node in the group
                curr = curr.next
            if curr:
                curr.next, curr = None, curr.next
        return res
        
    def count(self, head: ListNode | None) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        return count
        
        
        
        