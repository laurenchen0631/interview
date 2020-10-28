def bit_insert(n, m, i, j):
  head = n & (-1 << (j+1))
  middle = m << i
  tail = n & (1 << (i - 1)) if i > 0 else 0

  return head | middle | tail

print(f"{bit_insert(0b10000000000, 0b10011, 2, 6):b}")