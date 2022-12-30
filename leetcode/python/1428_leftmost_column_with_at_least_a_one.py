class BinaryMatrix(object):
   def get(self, row: int, col: int) -> int:
       pass
   def dimensions(self) -> list[]:
       pass

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: BinaryMatrix) -> int:
        m, n = binaryMatrix.dimensions()
        res = n
        for i in range(m):
            l, r = 0, n-1
            while l <= r:
                m = (l+r) // 2
                v = binaryMatrix.get(i, m)
                if v == 1:
                    r = m - 1
                else:
                    l = m + 1
            res = min(res, l)
        return res if res < n else -1