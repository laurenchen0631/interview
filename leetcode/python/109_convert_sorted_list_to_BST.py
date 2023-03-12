class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        return self.createTree(head, None)
    
    def createTree(self, head: ListNode | None, tail: ListNode | None) -> TreeNode | None:
        if head == tail:
            return None

        m = self.findMiddle(head, tail)
        root = TreeNode(m.val)
        root.left = self.createTree(head, m)
        root.right = self.createTree(m.next, tail)
        return root

    def findMiddle(self, head: ListNode | None, tail: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next 
        return slow