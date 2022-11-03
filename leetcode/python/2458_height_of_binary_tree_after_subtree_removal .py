# Definition for a binary tree node.
from collections import defaultdict
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # All the values in the tree are unique.
    def treeQueries(self, root: TreeNode | None, queries: list[int]) -> list[int]:
        depths, heights = defaultdict(int), defaultdict(int)

        def dfs(node, depth):
            if not node:
                return -1
            depths[node.val] = depth
            cur = max(dfs(node.left, depth + 1), dfs(node.right, depth + 1)) + 1
            heights[node.val] = cur
            return cur
        dfs(root, 0)

        # When a node is removed, the longest path rest passes its cousin that have the maximum height.
        cousins = {}
        for val, depth in depths.items():
            if depth not in cousins:
                cousins[depth] = []
            heapq.heappush(cousins[depth], (-heights[val], val))

        res = []
        for q in queries:
            depth = depths[q]
            if len(cousins[depth]) == 1:
                res.append(depth - 1)
            elif cousins[depth][0][1] == q:
                tmp = heapq.heappop(cousins[depth])
                res.append(-cousins[depth][0][0] + depth)
                # ?
                heapq.heappush(cousins[depth], tmp)
            else: 
                res.append(-cousins[depth][0][0] + depth)
        return res