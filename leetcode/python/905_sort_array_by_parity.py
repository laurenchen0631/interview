class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        return sorted(nums, key=lambda e: e & 1)

s = Solution()
print(s.sortArrayByParity([3,1,2,4]))