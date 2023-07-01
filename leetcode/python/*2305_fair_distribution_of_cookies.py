from sys import maxsize


class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        n = len(cookies)
        dist = [0] * k
        def dfs(i: int, zeroes: int) -> int:
            if n - i < zeroes:
                return maxsize
            if i == n:
                return max(dist)
            
            res = maxsize
            for j in range(k):
                dist[j] += cookies[i]
                v = dfs(i + 1, zeroes - (dist[j] == cookies[i]))
                res = min(res, v)
                dist[j] -= cookies[i]
            return res
        return dfs(0, k)
                