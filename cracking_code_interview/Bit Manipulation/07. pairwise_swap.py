pair_map = {
  0: 0,
  3: 3,
  1: 2,
  2: 1,
}

def pairwise_swap(n: int) -> int:
  result = 0
  count = 0
  while n != 0:
    result += pair_map[n & 3] << (count * 2)
    count += 1
    n >>= 2
  return result

def pairwise_swap_32bit(n: int) -> int:
  return ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)

print(bin(pairwise_swap(0b110110)))
print(bin(pairwise_swap_32bit(0b110110)))
print(bin(pairwise_swap(0b10110)))