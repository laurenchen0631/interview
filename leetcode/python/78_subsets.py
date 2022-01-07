class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        self.helper(nums, 0, [], res)
        return res

    def helper(self, nums: list[int], index: int, subset: list[int], res: list[list[int]]) -> None:
        if index >= len(nums):
            return res.append(subset.copy())

        subset.append(nums[index])
        self.helper(nums, index+1,  subset, res)
        subset.pop()
        self.helper(nums, index+1,  subset, res)

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))
    print(s.subsets([1]))