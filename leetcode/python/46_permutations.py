class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        self.helper(set[int](nums), [], res)
        return res
    
    def helper(self, nums: set[int], group: list[int], res: list[list[int]]) -> None:
        if len(nums) == 0:
            return res.append(group.copy())
        
        for n in nums:
            group.append(n)
            self.helper(nums.difference([n]), group, res)
            group.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
    print(s.permute([0,1]))
    print(s.permute([1]))