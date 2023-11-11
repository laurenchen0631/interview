import heapq


class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.graph = [[] for _ in range(n)]
        for u, v, w in edges:
            self.graph[u].append((v, w))

    def addEdge(self, edge: list[int]) -> None:
        u, v, w = edge
        self.graph[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        visited = [False] * len(self.graph)
        heap = [(0, node1)]
        while heap:
            dist, node = heapq.heappop(heap)
            if node == node2:
                return dist
            if visited[node]:
                continue
            visited[node] = True
            for neighbor, weight in self.graph[node]:
                heapq.heappush(heap, (dist + weight, neighbor))
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)