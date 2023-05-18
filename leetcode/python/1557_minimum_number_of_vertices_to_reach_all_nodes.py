class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        # count incoming edges for each node
        incoming = [0] * n
        for edge in edges:
            incoming[edge[1]] += 1
        # return nodes with no incoming edges
        return [i for i in range(n) if incoming[i] == 0]