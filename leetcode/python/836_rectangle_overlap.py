
Rect = tuple[int, int, int, int]

class Solution:
  def isRectangleOverlap(self, rec1: Rect, rec2: Rect) -> bool:
    # return rec2[0] < rec1[2] and rec2[2] > rec1[0] and rec2[1] < rec1[3] and rec2[3] > rec1[1]
    return not (rec1[2] <= rec2[0] or rec1[3] <= rec2[1] or rec1[0] >= rec2[2] or rec1[1] >= rec2[3])

if __name__ == '__main__':
  s = Solution()
  print(s.isRectangleOverlap([0, 0, 12, 8], [1, 3, 6, 7]))
  print(s.isRectangleOverlap([0, 0, 12, 8], [6, -4, 16, 0]))
  print(s.isRectangleOverlap([7,8,13,15], [10,8,12,20]))
  print(s.isRectangleOverlap([229,-132,833,333], [-244,-577,837,804]))
  