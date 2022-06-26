class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        res = cur = sum(cardPoints[:k])
        for i in range(k):
            cur = cur - cardPoints[k-1-i] + cardPoints[-i-1]
            res = max(res, cur)
        return res

s = Solution()
print(s.maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3))
print(s.maxScore(cardPoints = [2,2,2], k = 2))
print(s.maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7))