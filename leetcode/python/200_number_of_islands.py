class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        visited = set[tuple[int,int]]()
        count: int = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                q: list[tuple[int,int]] = []
                if grid[i][j] == '1' and (p := (i,j)) not in visited:
                    count += 1
                    q.append(p)
                
                while q:
                    (y,x) = p = q.pop()
                    if grid[y][x] == '0' or p in visited:
                        continue
                    visited.add(p)
                    if x > 0:
                        q.append((y, x-1))
                    if x < len(grid[0]) - 1:
                        q.append((y,x+1))
                    if y > 0:
                        q.append((y-1, x))
                    if y < len(grid) - 1:
                        q.append((y+1, x))
        
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]))

    print(s.numIslands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]))