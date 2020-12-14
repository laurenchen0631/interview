def find_path(grid):
  path = []
  visited = set()
  find_path_impl(grid, 0, 0, path, visited)
  path.reverse()
  
  return path if len(path) > 0 else None

def find_path_impl(grid, row, col, path, visited):
  if row >= len(grid) or col >= len(grid[0]) or is_off_limits(grid, row, col):
    return False

  p = (row, col)
  if is_goal(grid, row, col) or find_path_impl(grid, row + 1, col, path, visited) or find_path_impl(grid, row, col + 1, path, visited):
    path.append(p)
    return True
  
  visited.add(p)
  return False

def is_off_limits(grid, row, col):
  return grid[row][col] != 0

def is_goal(grid, row, col):
  return len(grid) == row + 1 and len(grid[0]) == col + 1

m1 = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 1, 0]
]

print(find_path(m1))