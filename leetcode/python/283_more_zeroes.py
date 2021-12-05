class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slot: int = 0
        cur: int = 0
        while cur < len(nums):
          if nums[cur] != 0:
            nums[slot], nums[cur] = nums[cur], nums[slot]
            slot += 1
          cur += 1

if __name__ == '__main__':
    s = Solution()
    a = [1,0,0,3,2]
    s.moveZeroes(a)
    print(a)

    b = [0, 1]
    s.moveZeroes(b)
    print(b)
          