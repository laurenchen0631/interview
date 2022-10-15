class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        b = f'{n:b}'
        cache: int = [1]
        for i in range(len(b)-1, -1, -1):
            if b[i] == '1':
                cache.append(cache[-1] * (1 << (len(b)-1-i)))
        res = []
        for l, r in queries:
            res.append((cache[r+1] // cache[l]) % (10**9+7))
        return res


s = Solution()
print(s.productQueries(15, [[0,1],[2,2],[0,3]]))
print(s.productQueries(n = 2, queries = [[0,0]]))
        