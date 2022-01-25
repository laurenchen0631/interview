class Solution:
    def rob(self, nums: list[int]) -> int:
        self.memo: dict[int, int] = {}
        return self.helper(nums, 0)

    def helper(self, houses: list[int], cur: int) -> int:
        if cur >= len(houses):
            return 0

        if cur in self.memo:
            return self.memo[cur]

        self.memo[cur] = max(
            houses[cur] + self.helper(houses, cur + 2),
            self.helper(houses, cur + 1),
        )
        return self.memo[cur]

    def robDP(self, nums: list[int]) -> int:
        skip = maxSteal = 0
        for n in nums:
            skip, maxSteal = maxSteal, max(skip + n, maxSteal)
        return maxSteal

      
if __name__ == '__main__':
  s = Solution()
  print(s.rob([1,2,3,1]))
  print(s.rob([2,7,9,3,1]))
  print(s.rob([1,2,3,4,1,6,100,3]))
  print(s.robDP([1,2,3,1]))
  print(s.robDP([2,7,9,3,1]))s
  print(s.robDP([1,2,3,4,1,6,100,3]))
