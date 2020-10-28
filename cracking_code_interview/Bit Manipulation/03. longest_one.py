def longest_one(num):
  bins = str(bin(num)).replace('0b', '')

  cursor = 0
  max_length = 0
  while cursor < len(bins) - max_length:
    length = 0
    start = cursor
    for b in bins[start:]:
      if b == '1':
        length += 1
      elif start == cursor:
        cursor = start + length + 1
        length += 1
      else:
        break
    max_length = max(length, max_length)
  
  return max_length

def longest_one_opt(num):
  current_length = 0
  prev_length = 0
  max_length = 1
  while num > 0:
    if num & 1 == 1:
      current_length += 1
    else:
      prev_length = 0 if (num & 0b10) == 0 else current_length
      current_length = 0
    max_length = max(prev_length + current_length + 1, max_length)
    num >>= 1
  return max_length

print(longest_one(1775))
print(longest_one_opt(1775))