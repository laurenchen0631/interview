def get_next(n: int) -> int:
  c = n
  c0 = 0
  c1 = 0
  while (c & 1) == 0 and c != 0:
    c0 += 1
    c >>= 1
  
  while (c & 1) == 1:
    c1 += 1
    c >>= 1
  
  if c0 + c1 == 0:
    return -1

  p = c0 + c1 # position of rightmost non-trailing zero
  n |= (1 << p) # flip rightmost non-trailing zero
  n &= ~((1 << p) - 1) # clear all bits to the right of p
  n |= (1 << (c1 - 1)) - 1

  return n

def get_prev(n: int) -> int:
  temp = 0
  c0 = 0
  c1 = 0
  while temp & 1 == 1:
    c1 += 1
    temp >>= 1

  if temp == 0:
    return -1
  
  while (temp & 1) == 0 and temp != 0:
    c0 += 1
    temp >>= 1

  p = c0 + c1
  n &= (~0 << (p + 1)) # clear from bit p onwards

  mask = (1 << (c1 + 1)) - 1
  n |= mask << (c0 - 1)

  return n

print(bin(get_next(13948)))