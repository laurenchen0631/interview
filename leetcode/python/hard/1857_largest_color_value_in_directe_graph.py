class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        N = len(colors)                                     # Number of nodes
        incoming, g = [0]*N, [[] for _ in range(N)]     # Define count for incoming edges, graph
        for u, v in edges:
            incoming[v]+=1
            g[u].append(v) 
        stack = [u for u in range(N) if incoming[u]==0]     # Populate stack with the nodes without incoming edges
        cnts = [[0]*26 for _ in range(N)]                   # Max. colors along all the incoming paths for the node 
        print(stack)

        while stack:                                        # While we have nodes to process
            u = stack.pop()                                 # Pop the next node to process
            print(u)
            cnts[u][ord(colors[u])-ord('a')] += 1           # Increment the color of the node itself
            for v in g[u]:                              # For all outgoing edges of the node
                cnts[v] = list(map(max, cnts[v], cnts[u]))
                incoming[v] -= 1
                if incoming[v]==0: stack.append(v)

        return -1 if sum(incoming)>0 else max([max(node) for node in cnts])

s = Solution()
# print(s.largestPathValue("hhqhuqhqff", [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]))
print(s.largestPathValue("hhqhuqh", [[0,1],[1,2],[2,3],[3,4],[5,2],[2,6]]))

# print(s.largestPathValue("a", [[0,0]]))
# print(s.largestPathValue(colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]))