def urlify(s: str, n: int) -> str:
  parts = list(s[:n]) # s[:n].split('')
  for i in range(len(parts)):
    if parts[i] == ' ':
      parts[i] = '%20'
  return ''.join(parts)

print(urlify("Mr John Smith    ", 13))