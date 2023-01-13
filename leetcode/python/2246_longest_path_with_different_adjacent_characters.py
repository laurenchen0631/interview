import heapq

class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        g = [[] for _ in range(len(parent))]
        for i in range(1, len(parent)):
            g[parent[i]].append(i)
        res = 0
        def dfs(node: int) -> int:
            heap = [0, 0]
            nonlocal res
            for child in g[node]:
                childPath = dfs(child)
                if s[node] == s[child]:
                    continue
                heapq.heappush(heap, childPath)
                if len(heap) > 2:
                    heapq.heappop(heap)
            secondLongest = heap[0] if heap else 0
            longest = heap[1] if heap else 0
            res = max(res, longest + secondLongest + 1)
            return longest + 1
        dfs(0)
        return res

s = Solution()
print(s.longestPath(parent = [-1,0,0,1,1,2], s = "abacbe"))
print(s.longestPath(parent = [-1,0,0,0], s = "aabc"))