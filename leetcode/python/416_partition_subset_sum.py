from functools import lru_cache

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total & 1 == 1:
          return False
        
        target = total // 2
        return self.dfs(tuple(nums), len(nums) - 1, target)

    @lru_cache(maxsize=None)
    def dfs(self, nums: tuple[int], n: int, target: int) -> bool:
        if target == 0:
            return True
        if n == 0 or target < 0:
            return False
        result = self.dfs(nums, n - 1, target - nums[n - 1]) or self.dfs(nums, n - 1, target)
        return result

    def canPartitionOpt(self, nums: list[int]) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2

        # construct a dp table of size (subset_sum + 1)
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]

        return dp[subset_sum]
        

if __name__ == '__main__':
    s = Solution()
    print(s.canPartition([1,5,5,11]))
    print(s.canPartition([1,2,3,5]))
    print(s.canPartition([2,2,3,5]))
    print(s.canPartition([1,2,3,4,5,6,7,8,9,9]))
    print(s.canPartition([14,9,8,4,3,2]))
    
    