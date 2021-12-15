class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        maxArea: int = 0
        stack: list[tuple[int,int]] = []
        visited = set[tuple[int,int]]()
        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j] == 1 and not (p := (i,j)) in visited:
                    stack.append(p)
                
                area: int = 0
                while len(stack) > 0:
                    (x,y) = p = stack.pop()
                    if p in visited:
                        continue

                    area += 1
                    visited.add(p)
                    if y + 1 < len(grid[0]) and grid[x][y+1] == 1:
                        stack.append((x, y+1))
                    if x + 1 < len(grid) and grid[x+1][y] == 1:
                        stack.append((x+1, y))
                    if y - 1 >= 0 and grid[x][y-1] == 1:
                        stack.append((x, y-1))
                    if x - 1 >= 0 and grid[x-1][y] == 1:
                        stack.append((x-1, y))
                maxArea = max(maxArea, area)
        return maxArea
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxAreaOfIsland([
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]))

    print(s.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))

    print(s.maxAreaOfIsland([
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]
    ]))

    print(s.maxAreaOfIsland([
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]))