import functools

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]

        @functools.lru_cache(None)
        def dp(left: int, right: int) -> int:
            if right < left:
                return 0
            
            res: int = 0
            for i in range(left, right + 1):
                gain = nums[left-1] * nums[i] * nums[right+1]
                remaining = dp(left,i-1) + dp(i+1, right)
                res = max(res, gain + remaining)

            return res

        return dp(1, len(nums) - 2)

    def maxCoinsBottomUp(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for l in range(len(nums)-2, 0, -1):
            for r in range(l, len(nums) - 1):
                dp[l][r] = max((dp[l][k-1] + dp[k+1][r] + nums[k]*nums[l-1]*nums[r+1]) for k in range(l, r+1))
        return dp[1][-2]

    
    

if __name__ == '__main__':
    s = Solution()
    print(s.maxCoins([3,1,5,8]))
    print(s.maxCoinsBottomUp([3,1,5,8]))