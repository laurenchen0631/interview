import sys

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0]) if m else 0
        dist = [[sys.maxsize] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    continue
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i < m - 1:
                    dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                if j < n - 1:
                    dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
        return dist

if __name__ == '__main__':
    s = Solution()
    print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))

                