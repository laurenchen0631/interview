class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return l



if __name__ == '__main__':
  s = Solution()
  print(s.searchInsert([1,3,5,6], 5))
  print(s.searchInsert([1,3,5,6], 2))
  print(s.searchInsert([1,3,5,6], 7))
  print(s.searchInsert([1,3,5,6], 0))
  print(s.searchInsert([1], 0))

        