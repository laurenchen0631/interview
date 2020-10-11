# Time: O(N), Space: O(N)
def is_perm(str1: str, str2: str) -> bool:
  if len(str1) != len(str2):
    return False
  chars = {}
  for c in str1:
    chars[c] = chars.get(c, 0) + 1
  for c in str2:
    if chars.get(c, 0) == 0:
      return False
    chars[c] -= 1

  return True

print(is_perm("abc", "cab"))
print(is_perm("aab", "baa"))
print(is_perm("cdabac", "abcdca"))
print(is_perm("abc", "bce"))