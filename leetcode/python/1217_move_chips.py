class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        even: int = 0
        odd: int = 0
        for p in position:
            if p & 1 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)

if __name__ == '__main__':
  s = Solution()
  print(s.minCostToMoveChips([1,2,3]))
  print(s.minCostToMoveChips([2,2,2,3,3]))
  print(s.minCostToMoveChips([1,1000000000]))
  print(s.minCostToMoveChips([1,2,2,2,3]))