def zero_matrix(mat):
  if len(mat) == 0:
    return

  zero_cols = set()
  zero_rows = set()
  for row in range(len(mat)):
    for col in range(len(mat[0])):
      if mat[row][col] == 0:
        if row not in zero_rows:
          make_zero_row_before(mat, row, col)
        if col not in zero_cols:
          make_zero_col_before(mat, row, col)
        zero_cols.add(col)
        zero_rows.add(row)
      
      elif row in zero_rows or col in zero_cols:
        mat[row][col] = 0

def make_zero_row_before(mat, row, col):
  for i in range(col):
    mat[row][i] = 0
  
def make_zero_col_before(mat, row, col):
  for i in range(row):
    mat[i][col] = 0

mat = [
  [1, 1, 1, 1, 1, 1],
  [1, 0, 1, 1, 0, 1],
  [0, 0, 1, 1, 1, 1]
]
zero_matrix(mat)
print(mat)