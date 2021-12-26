class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        points.sort(key=lambda p : p[0]**2 + p[1] ** 2)
        return points[:k]

if __name__ == '__main__':
    s = Solution()
    print(s.kClosest([[1,3],[-2,2]], 1))
    print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))