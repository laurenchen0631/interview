
class Solution:
    def numIslands(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        Pos = tuple[int, int]
        group = dict[Pos, Pos]()
        def union(u: Pos, v: Pos) -> bool:
            x = find(u)
            y = find(v)
            if x == y:
                return False
            group[x] = y
            return True
        def find(u: Pos) -> Pos:
            if u not in group:
                group[u] = u
            if group[u] != u:
                group[u] = find(group[u])
            return group[u]

        res = []
        count = 0
        for land in positions:
            land = tuple(land)
            if land not in group:
                group[land] = land
                count += 1
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nei = (land[0] + di, land[1] + dj)
                if nei in group and union(land, nei):
                    count -= 1
            res.append(count)
        return res

s = Solution()
print(s.numIslands(m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1],[0,2]]))