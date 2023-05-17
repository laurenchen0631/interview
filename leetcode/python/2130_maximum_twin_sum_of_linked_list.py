class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        res = 0
        for i in range(len(values) // 2):
            res = max(res, values[i] + values[-i - 1])
        return res