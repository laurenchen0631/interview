def flip_bit(a: int, b: int) -> int:
  count = 0
  while a != 0 or b != 0:
    if (a & 1) != (b & 1):
      count += 1
    a >>= 1
    b >>= 1

  return count

def flip_bit_opt(a: int, b: int) -> int:
  count = 0
  c = a ^ b 
  while c != 0:
    count += 1
    c &= c-1
  return count

print(flip_bit(0b11101, 0b1111))
print(flip_bit_opt(0b11101, 0b1111))
