class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        placeIndex = 0
        duplicates = [0, nums[0]]
        for n in nums:
            if n == duplicates[1] and duplicates[0] >= 2:
                continue
            
            nums[placeIndex] = n
            placeIndex += 1
            if n == duplicates[1]:
                duplicates[0] += 1
            else:
                duplicates = [1, n]
        return placeIndex

s = Solution()
a = [1,1,1,2,2,3]
print(s.removeDuplicates(a))
print(a)
b = [0,0,1,1,1,1,2,3,3]
print(s.removeDuplicates(b))
print(b)

