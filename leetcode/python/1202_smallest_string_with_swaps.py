from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        s = list(s)
        nodes = [i for i in range(len(s))]

        def find(x: int):
            if x == nodes[x]:
                return x
            nodes[x] = find(nodes[x])
            return nodes[x]

        def union(x: int, y: int):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                nodes[rooty] = rootx

        for e1, e2 in pairs:
            union(e1, e2)

        rootToComponent = defaultdict(list)

        for i in range(len(s)):
            root = find(i)
            rootToComponent[root].append(i)

        for _, indices in rootToComponent.items():
            chars = []
            for i in indices:
                chars.append(s[i])
            chars.sort()

            for c, i in zip(chars, indices):
                s[i] = c

        return ''.join(s)

s = Solution()
print(s.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]]))
print(s.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]]))
print(s.smallestStringWithSwaps(s = "cba", pairs = [[0,1],[1,2]]))