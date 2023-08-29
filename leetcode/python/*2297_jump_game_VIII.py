import sys


class Solution:
    # nums = [3,2,4,4,1]
    # costs = [3,7,6,4,2]
    def minCost(self, nums: list[int], costs: list[int]) -> int:
        case_one = []
        case_two = []
        dp = [sys.maxsize] * len(nums)
        dp[0] = 0

        for j in range(len(nums)):
            # nums[i] <= nums[j] and nums[k] < nums[i]
            while case_one and nums[j] >= nums[case_one[-1]]:
                dp[j] = min(dp[j], dp[case_one.pop()] + costs[j])
            # nums[i] > nums[j] and nums[k] >= nums[i]
            while case_two and nums[j] < nums[case_two[-1]]:
                dp[j] = min(dp[j], dp[case_two.pop()] + costs[j])
            
            case_one.append(j)
            case_two.append(j)
        return dp[-1]