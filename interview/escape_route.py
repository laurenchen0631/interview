
def solution(map):
    q: list[tuple[int,int,int]] = [(0, 0, 1)] # (x, y, breakable)
    visited = set([q[0]])
    count = 1
    while q:
        tmp = []
        for i, j, breakable in q:
            if i == len(map) - 1 and j == len(map[0]) - 1:
                return count
            
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ii, jj = i + di, j + dj
                if 0 <= ii < len(map) and 0 <= jj < len(map[0]):
                    if map[ii][jj] == 1 and breakable == 1:
                        tmp.append((ii, jj, 0))
                        visited.add((ii, jj, 0))
                    elif map[ii][jj] == 0 and (ii, jj, breakable) not in visited:
                        tmp.append((ii, jj, breakable))
                        visited.add((ii, jj, breakable))
        q = tmp
        count += 1
    return -1
    
print(solution([
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]))

# print(solution([
#     [0, 1, 1, 0],
#     [0, 0, 0, 1],
#     [1, 1, 0, 0],
#     [1, 1, 1, 0]
# ]))