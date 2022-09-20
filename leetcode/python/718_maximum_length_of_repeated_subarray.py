class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        res: int = 0
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    res = max(res, dp[i+1][j+1])
        return res

s = Solution()
print(s.findLength(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))
print(s.findLength([1,0,0,0,1], [1,0,0,1,1]))