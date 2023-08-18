class Solution:
    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        stack = [tuple(start)]
        dest = tuple(destination)
        visited = set()
        while stack:
            pos = stack.pop()
            if pos == dest:
                return True
            if pos in visited:
                continue
            visited.add(pos)
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                i, j = pos[0], pos[1]
                while 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] == 0:
                    i, j = i + dx, j + dy
                
                stack.append((i - dx, j - dy))
        return False
            
            