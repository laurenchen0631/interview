from typing import Counter


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = k
        n = len(answerKey)
        count = Counter(answerKey[:k])
        l = 0
        for r in range(k, n):
            count[answerKey[r]] += 1
            while min(count['T'], count['F']) > k:
                count[answerKey[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res