def str_compress(s: str) -> str:
  prev_c = ''
  acc = 0
  parts = []
  for c in s:
    if prev_c != c:
      if acc != 0:
        parts.append(f'{prev_c}{acc}')
      acc = 1
      prev_c = c
    else:
      acc += 1
  parts.append(f'{prev_c}{acc}')

  return ''.join(parts) if 2 * len(parts) < len(s) else s

print(str_compress('aabcccccaaa'))