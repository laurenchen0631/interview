
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid =  (l + r) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return -1

if __name__ == '__main__':
  s = Solution()
  print(s.search([1,2,3,4,5], 3))
  print(s.search([1,2,3,4,5], 1))
  print(s.search([1,2,3,4,5], -1))
  print(s.search([1,2,3,4,5], 5))
  print(s.search([1,2,3,4,5], 6))

  s = Solution()
  print(s.search([1,2,3,4,5,6], 3))
  print(s.search([1,2,3,4,5,6], 4))
  print(s.search([1,2,3,4,5,6], 5))

