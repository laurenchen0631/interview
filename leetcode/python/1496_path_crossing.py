class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cur = [0, 0]
        visited = set()
        for c in path:
            visited.add(tuple(cur))
            if c == 'N':
                cur[1] += 1
            elif c == 'S':
                cur[1] -= 1
            elif c == 'E':
                cur[0] += 1
            else:
                cur[0] -= 1
            if tuple(cur) in visited:
                return True
        return False
        