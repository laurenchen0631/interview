class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res: list[list[int]] = []
        candidates.sort()
        self.helper(candidates, target, 0, [], res)
        return res
    
    def helper(self, nums: list[int], target: int, i: int, comb: list[int], res: list[list[int]]) -> None:
        if target == 0:
            return res.append(comb.copy())
        
        while i < len(nums):
            n = nums[i]
            if target - n < 0:
                return
            comb.append(n)
            self.helper(nums, target-n, i+1, comb, res)
            comb.pop()
            i += 1
            while i < len(nums) and n == nums[i]:
                i += 1

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([2,3,6,7], 7))
    print(s.combinationSum2([2,3,5], 8))
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))
    print(s.combinationSum2([2,5,2,1,2], 5))
    print(s.combinationSum2([1,1], 1))