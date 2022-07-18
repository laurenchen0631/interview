from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        r, c = len(matrix), len(matrix[0])
        
        acc = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                acc[i][j] = acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1] + matrix[i - 1][j - 1]
        
        count = 0
        # reduce 2D problem to 1D one by fixing rows range
        for rt in range(1, r + 1):
            for rb in range(rt, r + 1):
                dp = defaultdict(int)
                dp[0] = 1
                
                for col in range(1, c + 1):
                    curSum = acc[rb][col] - acc[rt - 1][col]
                    # add subarrays to handle column range
                    count += dp[curSum - target]
                    dp[curSum] += 1
        return count

s = Solution()
print(s.numSubmatrixSumTarget(matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0))
print(s.numSubmatrixSumTarget(matrix = [[1,-1],[-1,1]], target = 0))