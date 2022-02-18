class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        dp = [1] * len(pairs)
        pairs.sort()
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

s = Solution()
print(s.findLongestChain([[1,2],[2,3],[3,4]]))
print(s.findLongestChain([[1,2],[7,8],[4,5]]))