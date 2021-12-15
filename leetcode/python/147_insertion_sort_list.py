# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        val: list[int] = []
        node = self
        while node != None:
            val.append(str(node.val))
            node = node.next
        return ' -> '.join(val)

class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        node = head
        while node:
            prev = dummy
            while prev.next and prev.next.val < node.val:
                prev = prev.next
            next = node.next
            node.next = prev.next
            prev.next = node

            node = next
        return dummy.next

if __name__ == '__main__':
  s = Solution()
  l1 = ListNode(4)
  l1.next = ListNode(2)
  l1.next.next = ListNode(1)
  l1.next.next.next = ListNode(3)
  print(s.insertionSortList(l1))