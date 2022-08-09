from math import sqrt


class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        arr.sort()
        n = len(arr)
        dp = [1] * n
        index = {arr[i]: i for i in range(n)}
        for i in arr[1:]:
            upper = sqrt(i)
            for j in arr[:i]:
                if j > upper:
                    break

                k, rem = divmod(i, j)
                if rem == 0 and k in index:
                    perm = dp[index[j]] * dp[index[k]]
                    dp[index[i]] += 2 * perm if j != k else perm
        return sum(dp) % (10 ** 9 + 7)

s = Solution()
print(s.numFactoredBinaryTrees([2, 4]))
print(s.numFactoredBinaryTrees([2, 4, 5, 10]))
print(s.numFactoredBinaryTrees([18,3,6,2]))