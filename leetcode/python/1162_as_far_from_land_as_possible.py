class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        q = list[tuple[int,int]]()
        visited = set[tuple[int,int]]()
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i,j))
                    visited.add((i,j))
        
        res = 0
        while q:
            tmp = list[tuple[int,int]]()
            for i,j in q:
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj = i+di,j+dj
                    if 0 <= ni < n and 0 <= nj < n and (ni,nj) not in visited:
                        tmp.append((ni,nj))
                        visited.add((ni,nj))
            res += 1
            q = tmp
        return res-1 if res > 1 else -1
    
s = Solution()
print(s.maxDistance([[1,0,0],[0,0,0],[0,0,0]]))