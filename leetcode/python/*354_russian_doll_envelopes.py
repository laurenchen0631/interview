from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        return self.LIS([e[1] for e in envelopes])
    
    def LIS(self, nums: list[int]) -> int:
        dp = []
        for n in nums:
            i = bisect_left(dp, n)
            if i == len(dp):
                dp.append(n)
            else:
                dp[i] = n
        return len(dp)
        
s = Solution()
print(s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(s.maxEnvelopes([[1,1],[1,1],[1,1]]))