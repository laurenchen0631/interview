class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        l: int = 0
        r = len(nums) - 1
        moves: int = 0
        while l < r:
            moves += nums[r] - nums[l]
            l += 1
            r -= 1
        return moves

s = Solution()
print(s.minMoves2([0,0,0,0,1000000]))