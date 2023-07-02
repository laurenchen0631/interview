class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        res = 0
        indegree = [0] * n
        def dfs(i: int, count: int) -> None:
            if i == len(requests):
                if all(v == 0 for v in indegree):
                    nonlocal res
                    res = max(res, count)
                return
            
            u, v = requests[i]
            indegree[u] -= 1
            indegree[v] += 1
            dfs(i + 1, count + 1)
            indegree[u] += 1
            indegree[v] -= 1
            dfs(i + 1, count)
        dfs(0, 0)
        return res
            