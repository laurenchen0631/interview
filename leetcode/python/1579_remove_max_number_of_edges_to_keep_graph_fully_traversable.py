class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        edgesRequired = 0
        
        for t, u, v in edges:
            if t == 3:
                edgesRequired += (alice.union(u, v) | bob.union(u, v))
                
        for t, u, v in edges:
            if t == 1:
                edgesRequired += alice.union(u, v)
            elif t == 2:
                edgesRequired += bob.union(u, v)
        
        if alice.count != 1 or bob.count != 1:
            return -1
        return len(edges) - edgesRequired
    
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.count = n
        
    def find(self, x: int):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        self.parent[rootX] = rootY
        self.count -= 1
        return True