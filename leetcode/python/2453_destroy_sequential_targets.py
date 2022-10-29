class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        rems: dict[int, tuple[int,int]] = {}
        for n in nums:
            r = n % space
            if r not in rems:
                rems[r] = (1, -n)
            else:
                rems[r] = (rems[r][0] + 1, -min(-rems[r][1], n))
        return -max(rems.values())[1] 
            
s = Solution()
print(s.destroyTargets(nums = [3,7,8,1,1,5], space = 2))
print(s.destroyTargets(nums = [1,3,5,2,4,6], space = 2))
print(s.destroyTargets(nums = [6,2,5], space = 2))