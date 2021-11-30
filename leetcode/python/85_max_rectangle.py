class Solution:

  # time: O(N^2 * M), space: O(NM).
  def maximalRectangle(self, matrix: list[list[str]]) -> int:
    maxArea: int = 0
    m: int = len(matrix)
    n: int = len(matrix[0]) if m > 0 else 0 
    dp: list[list[int]] = [[0] * n for _ in range(m)]

    for i in range(m):
      for j in range(n):
        if matrix[i][j] == '0':
          continue
        
        minWidth = dp[i][j] = dp[i][j-1] + 1 if j > 0 else 1

        for k in range(i, -1, -1):
          minWidth = min(minWidth, dp[k][j])
          maxArea = max(minWidth * (i - k + 1), maxArea)
    return maxArea

  # time: O(N*M), space: O(N).
  def maximalRectangleOpt(self, matrix: list[list[str]]) -> int:
      m = len(matrix)
      n = len(matrix[0]) if m > 0 else 0  

      left = [0] * n # initialize left as the leftmost boundary possible
      right = [n] * n # initialize right as the rightmost boundary possible
      height = [0] * n

      maxarea = 0

      for i in range(m):
          l: int = 0
          r: int = n
          for j in range(n):
            # update height and left
            if matrix[i][j] == '1':
              height[j] += 1
              # find the rightmost left 
              left[j] = max(left[j], l)
            else:
              height[j] = 0
              left[j] = 0
              l = j + 1

            # update right (reverse)
            k = n - j - 1
            if matrix[i][k] == '1':
              # find the leftmost right
              right[k] = min(right[k], r)
            else:
              right[k] = n
              r = k

          for j in range(n):
              maxarea = max(maxarea, height[j] * (right[j] - left[j]))

      return maxarea
      
if __name__ == '__main__':
  s = Solution()
  print(s.maximalRectangle([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
  ]))
  print(s.maximalRectangleOpt([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
  ]))