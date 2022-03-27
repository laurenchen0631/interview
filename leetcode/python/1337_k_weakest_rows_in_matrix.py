class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        rows: list[tuple[int,int]] = []
        for i, row in enumerate(mat):
            solider: int = 0
            for p in row:
                if p == 1:
                    solider += 1
                else:
                    break
            rows.append((solider, i))
        rows.sort()
        return [rows[j][1] for j in range(k)]

s = Solution()
print(s.kWeakestRows(mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], k = 2))

print(s.kWeakestRows(mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3))