# time: O(s), space: O(s)
def is_unique(s):
  chars = {}
  for c in s:
    if c in chars:
      return False
    chars[c] = True
  return True

print("abcdade", is_unique("abcdade"))
print("dbac", is_unique("dbac"))


# time: O(s log s), space: O(s)
def is_unique2(s):
  s = ''.join(sorted(s))
  for i in range(len(s) - 1):
    if s[i] == s[i+1]:
      return False
  return True  

print("abcdade", is_unique2("abcdade"))
print("dbac", is_unique2("dbac"))
