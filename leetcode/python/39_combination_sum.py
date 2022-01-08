class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res: list[list[int]] = []
        candidates.sort()
        self.helper(candidates, target, 0, [], res)
        return res
    
    def helper(self, nums: list[int], target: int, i: int, comb: list[int], res: list[list[int]]) -> None:
        if target == 0:
            return res.append(comb.copy())
        
        for i in range(i, len(nums)):
            n = nums[i]
            if target - n < 0:
                return
            comb.append(n)
            self.helper(nums, target-n, i, comb, res)
            comb.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))
    print(s.combinationSum([2,3,5], 8))
    print(s.combinationSum([2], 1))