from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> list[int]:
        freq = defaultdict(int)
        max_freq = 0
        
        q = deque([root])
        while q:
            node = q.popleft()
            freq[node.val] += 1
            max_freq = max(max_freq, freq[node.val])
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return [c for c, f in freq.items() if f == max_freq]
        
        