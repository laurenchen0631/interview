class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        nums.sort()
        self.helper(nums, 0, [], res)
        return res

    def helper(self, nums: list[int], index: int, subset: list[int], res: list[list[int]]) -> None:
        if index >= len(nums):
            return res.append(subset.copy())

        subset.append(nums[index])
        self.helper(nums, index+1,  subset, res)
        subset.pop()
        
        while index < len(nums) - 1 and nums[index] == nums[index+1]:
          index += 1
        self.helper(nums, index+1,  subset, res)

if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1,2,3]))
    print(s.subsetsWithDup([1,2,2]))
    print(s.subsetsWithDup([1,2,2,1]))