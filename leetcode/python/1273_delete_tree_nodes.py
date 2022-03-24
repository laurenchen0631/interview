from collections import defaultdict

class Solution:
    def deleteTreeNodes(self, nodes: int, parent: list[int], value: list[int]) -> int:
        if nodes == 0:
            return 0
        self.nodes = nodes
        children = defaultdict(list[int])
        for i in range(len(parent)):
            children[parent[i]].append(i)
        self.helper(0, children, value)
        return self.nodes
    
    def helper(self, i: int, children: dict[int, list[int]], value: list[int]) -> tuple[int, int]:
        total = value[i]
        count = 1
        for child in children[i]:
            (subtotal, nodes) = self.helper(child, children, value)
            total += subtotal
            count += nodes
        if total == 0:
            self.nodes -= count
            return (0, 0)
        return (total, count)