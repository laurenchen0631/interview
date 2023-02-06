class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        def getIndex(i: int):
            return 2 * i if i < n else 2 * (i - n) + 1
    
        for i in range(len(nums)):
            j = i
            while nums[i] >= 0:
                j = getIndex(j)
                nums[i], nums[j] = nums[j], -nums[i]
        for i in range(len(nums)):
            nums[i] = -nums[i]
        return nums
        
s = Solution()
print(s.shuffle([1,2,3,4,5,6,7,8], 4))