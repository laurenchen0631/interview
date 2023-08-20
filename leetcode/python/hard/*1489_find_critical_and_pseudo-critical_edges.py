class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.max_size = 1

    def find(self, x):
        # Finds the root of x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Connects x and y
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.max_size = max(self.max_size, self.size[root_x])
            return True
        return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        new_edges = sorted([[u, v, w, i] for i, (u, v, w) in enumerate(edges)], key=lambda x: x[2])

        # Find MST weight using union-find
        uf_std = UnionFind(n)
        std_weight = 0
        for u, v, w, _ in new_edges:
            if uf_std.union(u, v):
                std_weight += w

        # Check each edge for critical and pseudo-critical
        critical = []
        pseudo_critical = []
        for (u, v, w, i) in new_edges:
            # Ignore this edge and calculate MST weight
            uf_ignore = UnionFind(n)
            ignore_weight = 0
            for (x, y, w_ignore, j) in new_edges:
                if i != j and uf_ignore.union(x, y):
                    ignore_weight += w_ignore
            # If the graph is disconnected or the total weight is greater,
            # the edge is critical
            if uf_ignore.max_size < n or ignore_weight > std_weight:
                critical.append(i)
                continue

            # Force this edge and calculate MST weight
            uf_force = UnionFind(n)
            force_weight = w
            uf_force.union(u, v)
            for (x, y, w_force, j) in new_edges:
                if i != j and uf_force.union(x, y):
                    force_weight += w_force
            # If total weight is the same, the edge is pseudo-critical
            if force_weight == std_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]
    
s = Solution()
print(s.findCriticalAndPseudoCriticalEdges(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]))