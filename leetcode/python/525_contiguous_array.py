class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        loc: dict[int.int] = {0: -1}
        maxLength: int = 0
        count: int = 0
        for i in range(len(nums)):
            count = count + (1 if nums[i] == 1 else -1)
            if count in loc:
                maxLength = max(maxLength, i - loc[count])
            else:
                loc[count] = i
        return maxLength

s = Solution()
print(s.findMaxLength([0,1]))
print(s.findMaxLength([0, 1, 0]))
print(s.findMaxLength([0, 1, 0, 1, 1, 1, 0, 0, 1, 0]))