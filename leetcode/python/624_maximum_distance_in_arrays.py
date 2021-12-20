class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        if len(arrays) < 2:
            return 0
        
        res: int = 0
        curMin = arrays[0][0]
        curMax = arrays[0][-1]
        
        for arr in arrays[1:]:
            res = max(res, abs(arr[0] - curMax), abs(arr[-1] - curMin))
            curMax = max(curMax, arr[-1])
            curMin = min(curMin, arr[0])
        
        return res

if __name__ == '__main__':
  s = Solution()
  print(s.maxDistance([[1,2,3],[4,5],[1,2,3]]))
  print(s.maxDistance([[1],[1]]))
  print(s.maxDistance([[1],[2]]))
  print(s.maxDistance([[1,4],[0,5]]))
  print(s.maxDistance([[-1,4],[-5,6]]))