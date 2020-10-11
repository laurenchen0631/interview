def is_one_away(s1: str, s2: str) -> bool:
  if s1 == s2:
    return True
  
  if len(s1) > len(s2):
    (s1, s2) = (s2, s1)

  if (diff := len(s2) - len(s1)) < 2:
    # return is_one_replace(s1, s2) if diff == 0 else is_one_insert(s1, s2)
    offset = 0
    for i in range(len(s1)):
      if s1[i] != s2[(0 if diff == 0 else offset) + i]:
        offset += 1
        if offset > 1:
          return False
    return True

  return False

def is_one_replace(s1, s2):
  diff = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      diff += 1
      if diff > 1:
        return False
  return True

def is_one_insert(s1, s2):
  diff = 0
  for i in range(len(s1)):
    if s1[i] != s2[diff + i]:
      diff += 1
      if diff > 1:
        return False
  return True

print(is_one_away("abcd", "abcde"))
print(is_one_away("abcde", "abcd"))
print(is_one_away("abcd", "abed"))
print(is_one_away("pale", "ple"))
print(is_one_away("pales", "pale"))
print(is_one_away("pale", "bale"))
print(is_one_away("pale", "bake"))