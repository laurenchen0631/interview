from inspect import stack


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        rows = dict[int, set[tuple[int, int]]]()
        cols = dict[int, set[tuple[int, int]]]()
        for p in stones:
            p = tuple(p)
            rows[p[0]] = rows.get(p[0], set())
            rows[p[0]].add(p)
            cols[p[1]] = cols.get(p[1], set())
            cols[p[1]].add(p)

        visited = set[tuple[int, int]]()
        res: int = 0
        for p in stones:
            p = tuple(p)
            if p in visited:
                continue
            stack = [p]
            visited.add(p)
            size: int = 0
            while stack:
                size += 1
                p = stack.pop()
                for p2 in rows[p[0]]:
                    if p2 not in visited:
                        stack.append(p2)
                        visited.add(p2)
                rows[p[0]].clear()

                for p2 in cols[p[1]]:
                    if p2 not in visited:
                        stack.append(p2)
                        visited.add(p2)
                cols[p[1]].clear()
            res += size - 1
        return res

s = Solution()
print(s.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
print(s.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
print(s.removeStones([[0,1],[1,0]]))
print(s.removeStones([[0,1],[1,0],[1,1]]))
                

                
        