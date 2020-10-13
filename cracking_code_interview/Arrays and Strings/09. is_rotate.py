def is_rotate(s1: str, s2: str) -> bool:
  if len(s1) != len(s2):
    return False
  if s1 == s2:
    return True

  pivot = 1
  while pivot < len(s1):
    if s1[:pivot] in s2:
      pivot += 1
    else:
      break
  return True if s1[pivot:] in s2 else False

def is_rotate_opt(s1: str, s2: str) -> bool:
  if (len(s1) == len(s2)):
    return s2 in s1 + s1
  return False

print(is_rotate('waterbottle', 'erbottlewat'))
print(is_rotate('waterbottle', 'erbottdewat'))

print(is_rotate_opt('waterbottle', 'erbottlewat'))
print(is_rotate_opt('waterbottle', 'erbottdewat'))