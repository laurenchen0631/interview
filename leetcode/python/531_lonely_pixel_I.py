class Solution:
    def findLonelyPixel(self, picture: list[list[str]]) -> int:
        blacks: list[tuple[int,int]] = []
        m, n = len(picture), len(picture[0])
        row = [0] * m
        col = [0] * n
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'W':
                    continue
                if row[i] == col[j] == 0:
                    blacks.append((i, j))
                row[i] += 1
                col[j] += 1
        
        return sum([1 if row[i] == col[j] == 1 else 0 for i, j in blacks])
        