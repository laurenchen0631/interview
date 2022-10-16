
class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        res = 0
        mini = maxi = -1
        j = 0
        for i, n in enumerate(nums):
            if not minK <= n <= maxK:
                mini = maxi = -1
                j = i + 1
            if n == minK:
                mini = i
            if n == maxK:
                maxi = i

            res += max(0, min(mini, maxi) - j + 1)

        return res


s = Solution()
print(s.countSubarrays(nums = [3,1,5,2,0,7,5,2,1], minK = 1, maxK = 5))
print(s.countSubarrays(nums = [1,3,5,2,0,7,5], minK = 1, maxK = 5))
print(s.countSubarrays(nums = [1,1,1,1], minK = 1, maxK = 1))
print(s.countSubarrays([35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913], 35054, 945315))