def is_palindrome_perm(s: str) -> bool:
  s = normalize_str(s)
  # chars = list(0 for _ in range(256))
  odds_char = set()
  
  for c in s:
    if c in odds_char:
      odds_char.remove(c)
    else:
      odds_char.add(c) 

  return len(odds_char) < 2

def normalize_str(s: str) -> str:
  s = s.lower()
  return ''.join(s.split())

print(is_palindrome_perm('Tact Coa'))
print(is_palindrome_perm('tactcoapapa'))
print(is_palindrome_perm('abc'))