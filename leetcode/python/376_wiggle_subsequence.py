class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        dpPos = [1] * len(nums)
        dpNeg = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] == nums[i]:
                    dpPos[i] = max(dpPos[i], dpPos[j])
                    dpNeg[i] = max(dpNeg[i], dpNeg[j])
                elif nums[j] < nums[i]: # -
                    dpNeg[i] = max(dpNeg[i], dpPos[j] + 1)
                else:
                    dpPos[i] = max(dpPos[i], dpNeg[j] + 1)
        return max(dpPos[-1], dpNeg[-1])

s = Solution()
print(s.wiggleMaxLength([1,7,4,9,2,5]))
print(s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
print(s.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))