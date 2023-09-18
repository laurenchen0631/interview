class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        weakest = []
        for i, row in enumerate(mat):
            n = self.count_solider(row)
            print(n)
            weakest.append((n, i))
        weakest.sort()
        return [i for n, i in weakest[:k]]

    def count_solider(self, arr: list[int]) -> int:
        l, r = 0, len(arr)
        while l < r:
            m = (l+r) // 2
            if arr[m] == 1:
                l = m + 1
            else:
                r = m
        return l

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