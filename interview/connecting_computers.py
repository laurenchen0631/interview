def minOperations(comp_nodes: int, comp_from: list[int], comp_to: list[int]) -> int:
    n, m = comp_nodes, len(comp_from)
    g = {i: [] for i in range(1, n + 1)}
    for i in range(m):
        g[comp_from[i]].append(comp_to[i])
        g[comp_to[i]].append(comp_from[i])
    
    visited = set()
    count_groups = count_edges = 0
    for i in range(1, n + 1):
        if i in visited:
            continue
        # visit the group
        stack = [i]
        count = 0
        while stack:
            u = stack.pop()
            if u in visited:
                continue
            visited.add(u)
            count += 1
            for v in g[u]:
                if v not in visited:
                    stack.append(v)
        count_groups += 1
        count_edges += count - 1

    return count_groups -1 if m - count_edges >= count_groups - 1 else -1
    
print(minOperations(4, [1,3], [2,4]))
print(minOperations(4, [1,1,3], [2,3,2]))