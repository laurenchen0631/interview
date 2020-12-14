def get_subsets(arr: list[int], index: int) -> list[set[int]]:
  # Base case - add empty set
  if len(arr) == index:
    print('add empty')
    return [set()]
  
  subsets = get_subsets(arr, index + 1)
  value = arr[index]
  tmp: list = []

  for subset in subsets:
    copy: set[int] = subset.copy()
    copy.add(value)
    tmp.append(copy)
  subsets.extend(tmp)
  print('add ', tmp)

  return subsets

# print(get_subsets([1, 2, 3], 0))
print(get_subsets([1, 2, 3, 4], 0))