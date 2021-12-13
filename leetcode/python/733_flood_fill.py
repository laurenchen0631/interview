
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        oldColor: int = image[sr][sc]
        m = len(image)
        n = len(image[0]) if m > 0 else 0
        stack: list[tuple[int, int]] = [(sr, sc)]
        visited = set[tuple[int, int]]()
        
        while len(stack) > 0:
            (x, y) = p = stack.pop()
            visited.add(p)
            
            if image[x][y] != oldColor:
                continue

            image[x][y] = newColor
            if x > 0 and not (t := (x-1, y)) in visited:
                stack.append(t)
            if y < n - 1 and not (t := (x, y+1)) in visited:
                stack.append(t)
            if x < m - 1 and not (t := (x+1, y)) in visited:
                stack.append(t)
            if y > 0 and not (t := (x, y-1)) in visited:
                stack.append(t)

        return image

if __name__ == '__main__':
  s = Solution()
  print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
  print(s.floodFill([[0,0,0],[0,0,0]], 0, 0, 2))