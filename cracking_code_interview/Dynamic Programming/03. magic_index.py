def get_magic_index(sorted_arr: list[int]):
  left = 0
  right = len(sorted_arr) - 1
  while left < right:
    index = round((left + right) / 2)
    if sorted_arr[index] == index:
      return index
    elif sorted_arr[index] > index:
      right = index 
    else:
      left = index
  return None

print(get_magic_index([1, 2, 3, 4, 5]))
print(get_magic_index([-5, -3, -2, 0, 4]))
print(get_magic_index([-10, 1, 5, 10, 12, 15]))
print(get_magic_index([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]))

def magic_fast(arr: list[int]) -> int:
  return magic_fast_impl(arr, 0, len(arr) - 1)

def magic_fast_impl(arr: list[int], start: int, end: int) -> int:
  if end < start:
    return None
  
  index = round((start + end) / 2)
  value = arr[index]
  if index == value:
    return index
  
  left_index = min(index - 1, value)
  if i := magic_fast_impl(arr, start, left_index):
    return i

  right_index = max(index + 1, value)
  if i := magic_fast_impl(arr, right_index, end):
    return i

print(magic_fast([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]))
print(magic_fast([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]))