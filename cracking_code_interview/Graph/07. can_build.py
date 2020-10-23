def can_build(projects, dependencies):
  deps = {p: set() for p in projects}
  for (req, p) in dependencies:
    deps[p].add(req)

  order = []
  while (projs := build(deps)) and len(projs) > 0:
    order.extend(projs)
    for p in projs:
      del deps[p]

    for p in deps.keys():
      deps[p] = deps[p].difference(projs)

  if len(deps) > 0:
    return None
  return order

def build(deps):
  results = []
  for p in deps.keys():
    dep = deps[p]
    if len(dep) == 0:
      results.append(p)
  return results

out = can_build(
  ['a', 'b', 'c', 'd', 'e', 'f'],
  [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
)
print(out)