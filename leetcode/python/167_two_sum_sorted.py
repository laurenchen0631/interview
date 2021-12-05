class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while (sum := numbers[left] + numbers[right]) != target:
          if target < sum:
            right -= 1
          else:
            left += 1

        return [left+1, right+1]

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([2,3,4], 6))
    print(s.twoSum([-2, -1, 0, 3], -1))
    
    