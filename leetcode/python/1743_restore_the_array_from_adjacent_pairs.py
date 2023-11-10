from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        g = defaultdict(list[int])
        start = set[int]()
        for u, v in adjacentPairs:
            if u in start:
                start.remove(u)
            else:
                start.add(u)
            if v in start:
                start.remove(v)
            else:
                start.add(v)
            g[u].append(v)
            g[v].append(u)

        res = []
        prev = None
        node = start.pop()
        while len(res) < len(adjacentPairs) + 1:
            res.append(node)
            for nei in g[node]:
                if nei != prev:
                    prev = node
                    node = nei
                    break
        return res