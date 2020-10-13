def rotate_90(m):
  if len(m) < 2 or len(m) != len(m[0]):
    return

  n = len(m)
  r = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      r[j][n-1-i] = m[i][j]
  
  for i in range(n):
    m[i] = r[i]

def rotate_90_opt(m):
  if len(m) < 2 or len(m) != len(m[0]):
    return

  n = len(m)
  for layer in range(n // 2):
    first = layer
    last = n - 1 - layer
    for i in range(first, last):
      top = m[first][i]
      offset = i - first

      # left -> top
      m[first][i] = m[last - offset][first]
      # bottom -> left
      m[last - offset][first] = m[last][last-offset]
      # right -> bottom
      m[last][last-offset] = m[i][last]
      # top -> right
      m[i][last] = top

mat1 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16],
]

mat2 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16],
]

rotate_90(mat1)
print(mat1)

rotate_90_opt(mat2)
print(mat2)