cache = {
  0: 0,
  1: 1,
  2: 2,
  3: 4,
}

def climb(n):
  if n < 0:
    return 0

  if n not in cache:
    cache[n] = climb(n - 1) + climb(n - 2) + climb(n - 3)
  
  return cache[n]