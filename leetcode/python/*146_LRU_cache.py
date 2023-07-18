from __future__ import annotations

class ListNode:
    def __init__(
        self,
        key: int = -1, val: int = -1,
        prev: ListNode | None = None, nxt: ListNode | None = None
    ):
        self.key = key
        self.val = val
        self.next, self.prev = nxt, prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._size = 0
        self.cache = dict[int, ListNode]()
        self._head = ListNode()
        self._tail = ListNode()
        self._head.next = self._tail
        self._tail.prev = self._head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            self._size += 1
            if self._size > self.capacity:
                self._remove_tail()
    
    def _move_to_head(self, node: ListNode) -> None:
        self._remove_node(node)
        self._add_to_head(node)
        
    def _remove_node(self, node: ListNode) -> None:
        if node.prev and node.prev.next:
            node.prev.next = node.next
        if node.next and node.next.prev:
            node.next.prev = node.prev
            
    def _add_to_head(self, node: ListNode) -> None:
        node.next = self._head.next
        node.prev = self._head
        if self._head.next:
            self._head.next.prev = node
        self._head.next = node

    def _remove_tail(self) -> None:
        node = self._tail.prev
        if node:
            self._remove_node(node)
            del self.cache[node.key]
            self._size -= 1
        
