class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, i, res)
        return res
    
    def twoSum(self, nums: list[int], i: int, res: list[list[int]]):
        low = i + 1
        high = len(nums) - 1
        while low < high:
            t = nums[i] + nums[low] + nums[high]
            if t < 0:
                low += 1
            elif t > 0:
                high -= 1
            else:
                res.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low-1]:
                    low += 1

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))